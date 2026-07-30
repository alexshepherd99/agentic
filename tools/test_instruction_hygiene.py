"""Tests for the instruction-hygiene parsers.

Run from the repo root::

    python3 -m unittest discover -s tools

Scope is the pure parsing and threshold logic. ``check_references`` and
``check_duplication`` need fixture repo trees and are not covered.
"""

import pathlib
import tempfile
import textwrap
import unittest

import instruction_hygiene


def dedent(text: str) -> str:
    """Fixture helper: strip the indentation an inline literal carries."""
    return textwrap.dedent(text).lstrip("\n")


class WriteFileMixin:
    """Gives a test case a scratch directory and a file-writing helper."""

    def setUp(self) -> None:
        self.directory = pathlib.Path(tempfile.mkdtemp())

    def write(self, name: str, text: str) -> pathlib.Path:
        """Write ``text`` to ``name`` inside the scratch directory."""
        path = self.directory / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(dedent(text))
        return path


class StripCodeTest(unittest.TestCase):
    def test_drops_fenced_block(self) -> None:
        text = dedent(
            """
            before
            ```
            threshold = 3
            ```
            after
            """
        )
        stripped = instruction_hygiene.strip_code(text)
        self.assertNotIn("threshold", stripped)
        self.assertIn("before", stripped)
        self.assertIn("after", stripped)

    def test_fenced_block_contributes_no_words(self) -> None:
        """The inline rule would leave ``X`` tokens behind; the fence rule leaves none."""
        stripped = instruction_hygiene.strip_code("```thresholds\nthreshold = 3\n```\n")
        self.assertEqual(stripped.split(), [])

    def test_reduces_inline_span_to_one_token(self) -> None:
        stripped = instruction_hygiene.strip_code("run `python3 tools/x.py` now")
        self.assertEqual(stripped, "run X now")

    def test_html_comment_contributes_no_words(self) -> None:
        """An override marker is metadata; measuring it makes overriding self-defeating."""
        marker = "<!-- hygiene-ok: sentence_max_words — a long stated reason here. 2026-07-30 -->"
        self.assertEqual(instruction_hygiene.strip_code(marker).split(), [])


class SplitFrontmatterTest(unittest.TestCase):
    def test_splits_when_present(self) -> None:
        frontmatter, body = instruction_hygiene.split_frontmatter(
            dedent(
                """
                ---
                name: thing
                ---
                # Body
                """
            )
        )
        self.assertEqual(frontmatter, "name: thing")
        self.assertEqual(body, "# Body\n")

    def test_absent_frontmatter_yields_whole_text_as_body(self) -> None:
        frontmatter, body = instruction_hygiene.split_frontmatter("# Body\n")
        self.assertEqual(frontmatter, "")
        self.assertEqual(body, "# Body\n")

    def test_unterminated_frontmatter_is_treated_as_body(self) -> None:
        text = "---\nname: thing\n# Body\n"
        frontmatter, body = instruction_hygiene.split_frontmatter(text)
        self.assertEqual(frontmatter, "")
        self.assertEqual(body, text)


class BlocksTest(unittest.TestCase):
    def test_each_list_item_is_its_own_block(self) -> None:
        found = instruction_hygiene.blocks("- first rule\n- second rule\n")
        self.assertEqual(found, ["- first rule", "- second rule"])

    def test_continuation_line_stays_with_its_item(self) -> None:
        found = instruction_hygiene.blocks("- first rule\n  still the first rule\n")
        self.assertEqual(found, ["- first rule\n  still the first rule"])

    def test_heading_and_blank_line_end_a_block(self) -> None:
        found = instruction_hygiene.blocks(
            dedent(
                """
                a paragraph
                # Heading
                another paragraph

                a third paragraph
                """
            )
        )
        self.assertEqual(found, ["a paragraph", "another paragraph", "a third paragraph"])

    def test_fenced_content_is_excluded(self) -> None:
        found = instruction_hygiene.blocks(
            dedent(
                """
                a paragraph
                ```
                - not a rule
                ```
                """
            )
        )
        self.assertEqual(found, ["a paragraph"])


class SentencesTest(unittest.TestCase):
    """Markup must not be measured as prose. Every case here is a fixed defect."""

    def test_bold_lead_in_label_is_its_own_sentence(self) -> None:
        found = instruction_hygiene.sentences("- **Rule.** Detail here.")
        self.assertEqual(found, ["Rule.", "Detail here."])

    def test_list_marker_is_not_a_word(self) -> None:
        found = instruction_hygiene.sentences("- Collapsing for small efforts")
        self.assertEqual(found, ["Collapsing for small efforts"])

    def test_numbered_marker_is_not_a_sentence(self) -> None:
        found = instruction_hygiene.sentences("4. **Verify it holds.** Try it.")
        self.assertEqual(found, ["Verify it holds.", "Try it."])

    def test_splits_before_a_quoted_sentence_start(self) -> None:
        found = instruction_hygiene.sentences('It settles. "The change" is obvious.')
        self.assertEqual(found, ["It settles.", '"The change" is obvious.'])

    def test_still_splits_before_a_bold_mid_block_label(self) -> None:
        found = instruction_hygiene.sentences("Ruled out above. **Non-negotiable:** do it.")
        self.assertEqual(found, ["Ruled out above.", "Non-negotiable: do it."])

    def test_period_inside_a_code_span_is_not_a_boundary(self) -> None:
        found = instruction_hygiene.sentences("Read `learning/CONVENTIONS.md` first.")
        self.assertEqual(found, ["Read X first."])

    def test_each_line_of_a_block_is_segmented_independently(self) -> None:
        found = instruction_hygiene.sentences("- first rule\n  a continuation")
        self.assertEqual(found, ["first rule", "a continuation"])


class OverridesTest(unittest.TestCase):
    def test_parses_metric_from_em_dash_form(self) -> None:
        text = "<!-- hygiene-ok: block_max_words — carries a boundary. 2026-07-30 -->"
        self.assertEqual(instruction_hygiene.overrides(text), {"block_max_words"})

    def test_parses_metric_from_double_hyphen_form(self) -> None:
        text = "<!-- hygiene-ok: file_max_words -- long by design. 2026-07-30 -->"
        self.assertEqual(instruction_hygiene.overrides(text), {"file_max_words"})

    def test_collects_every_metric_in_the_file(self) -> None:
        text = dedent(
            """
            <!-- hygiene-ok: block_max_words — one. 2026-07-30 -->
            <!-- hygiene-ok: sentence_max_words — two. 2026-07-30 -->
            """
        )
        self.assertEqual(
            instruction_hygiene.overrides(text),
            {"block_max_words", "sentence_max_words"},
        )

    def test_no_marker_yields_nothing(self) -> None:
        self.assertEqual(instruction_hygiene.overrides("plain prose"), set())


class LoadThresholdsTest(WriteFileMixin, unittest.TestCase):
    def test_parses_fence_and_strips_trailing_comment(self) -> None:
        doc = self.write(
            "hygiene.md",
            """
            # Doc
            ```thresholds
            sentence_max_words = 25
            file_max_words     = 800  # a backstop
            ```
            """,
        )
        self.assertEqual(
            instruction_hygiene.load_thresholds(doc),
            {"sentence_max_words": 25, "file_max_words": 800},
        )

    def test_missing_doc_raises(self) -> None:
        with self.assertRaises(FileNotFoundError):
            instruction_hygiene.load_thresholds(self.directory / "absent.md")

    def test_missing_fence_raises(self) -> None:
        doc = self.write("hygiene.md", "# Doc\n\nno thresholds here\n")
        with self.assertRaises(ValueError):
            instruction_hygiene.load_thresholds(doc)

    def test_empty_fence_raises(self) -> None:
        doc = self.write("hygiene.md", "```thresholds\n```\n")
        with self.assertRaises(ValueError):
            instruction_hygiene.load_thresholds(doc)


class CheckFileTest(WriteFileMixin, unittest.TestCase):
    LIMITS = {
        "sentence_max_words": 5,
        "block_max_words": 10,
        "nonneg_max_density_pct": 25,
        "file_max_words": 20,
        "description_max_words": 4,
    }

    def flags(self, text: str, name: str = "SKILL.md") -> dict[str, int]:
        """Metric name to flagged value, for a file holding ``text``."""
        path = self.write(name, text)
        found = instruction_hygiene.check_file(path, self.directory, self.LIMITS)
        return {flag.metric: flag.value for flag in found}

    def test_sentence_over_limit_flags_and_reports_its_length(self) -> None:
        flags = self.flags("one two three four five six\n")
        self.assertEqual(flags.get("sentence_max_words"), 6)

    def test_sentence_at_limit_is_quiet(self) -> None:
        self.assertNotIn("sentence_max_words", self.flags("one two three four five\n"))

    def test_block_over_limit_flags(self) -> None:
        block = " ".join(["word"] * 11) + "\n"
        self.assertEqual(self.flags(block).get("block_max_words"), 11)

    def test_block_at_limit_is_quiet(self) -> None:
        block = " ".join(["word"] * 10) + "\n"
        self.assertNotIn("block_max_words", self.flags(block))

    def test_block_word_count_includes_the_list_marker(self) -> None:
        """Unlike the sentence count, a block counts ``- `` as one of its words."""
        block = "- " + " ".join(["word"] * 10) + "\n"
        self.assertEqual(self.flags(block).get("block_max_words"), 11)

    def test_file_over_limit_flags_body_words_only(self) -> None:
        body = "\n\n".join(" ".join(["word"] * 7) for _ in range(3))
        flags = self.flags(f"---\nname: thing\n---\n{body}\n")
        self.assertEqual(flags.get("file_max_words"), 21)

    def test_description_word_count_comes_from_frontmatter(self) -> None:
        flags = self.flags("---\ndescription: one two three four five\n---\nbody\n")
        self.assertEqual(flags.get("description_max_words"), 5)

    def test_multiline_description_is_counted_whole(self) -> None:
        text = dedent(
            """
            ---
            description: one two
              three four five
            name: thing
            ---
            body
            """
        )
        self.assertEqual(self.flags(text).get("description_max_words"), 5)

    def test_non_negotiable_density_flags_above_threshold(self) -> None:
        text = "- **Non-negotiable:** do it\n- a rule\n- another rule\n"
        self.assertEqual(self.flags(text).get("nonneg_max_density_pct"), 33)

    def test_non_negotiable_density_within_threshold_is_quiet(self) -> None:
        text = "- **Non-negotiable:** do it\n- a rule\n- another\n- one more\n"
        self.assertNotIn("nonneg_max_density_pct", self.flags(text))

    def test_override_suppresses_only_its_own_metric(self) -> None:
        text = dedent(
            """
            <!-- hygiene-ok: sentence_max_words — carries a boundary. 2026-07-30 -->
            - one two three four five six seven eight nine ten eleven
            """
        )
        flags = self.flags(text)
        self.assertNotIn("sentence_max_words", flags)
        self.assertIn("block_max_words", flags)

    def test_flag_carries_the_repo_relative_path(self) -> None:
        path = self.write("skills/thing/SKILL.md", "one two three four five six\n")
        found = instruction_hygiene.check_file(path, self.directory, self.LIMITS)
        self.assertEqual(found[0].path, "skills/thing/SKILL.md")


class CountInstructionsTest(WriteFileMixin, unittest.TestCase):
    def test_counts_list_lines_and_ignores_fenced_content(self) -> None:
        path = self.write(
            "SKILL.md",
            """
            ---
            name: thing
            ---
            - first rule
            - second rule
              - a nested rule
            ```
            - not a rule
            ```
            a paragraph
            """,
        )
        self.assertEqual(instruction_hygiene.count_instructions([path]), 3)

    def test_frontmatter_lines_are_not_instructions(self) -> None:
        path = self.write("SKILL.md", "---\nname: thing\n---\n- only rule\n")
        self.assertEqual(instruction_hygiene.count_instructions([path]), 1)


class SummariseTest(unittest.TestCase):
    def test_collapses_whitespace_and_truncates(self) -> None:
        self.assertEqual(instruction_hygiene.summarise("a\n  b   c", width=3), "a b")


if __name__ == "__main__":
    unittest.main()
