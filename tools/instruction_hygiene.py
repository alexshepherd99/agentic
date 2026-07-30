"""Report instruction-hygiene flags for this repo's instruction content.

Thresholds are read from ``shared/instruction-hygiene.md`` so they exist in
exactly one place. Run from the repo root::

    python3 tools/instruction_hygiene.py

Exits 0 always: a flag is a prompt to look, never a gate.
"""

import dataclasses
import logging
import pathlib
import re
import sys

LOGGER = logging.getLogger("instruction_hygiene")

THRESHOLDS_DOC = pathlib.Path("shared/instruction-hygiene.md")

# Referenced by runtime files but living in a consuming project, not here.
PROJECT_LOCAL_DOCS = frozenset(
    {
        "BACKLOG.md",
        "log.md",
        "plan.md",
        "requirements.md",
        "agent.md",
        ".github/copilot-instructions.md",
    }
)

# Loaded by humans, never at skill runtime.
NON_RUNTIME_DOCS = ("learning/CONVENTIONS.md", "learning/INBOX.md")

# A bare mention is fine (CLAUDE.md describes the repo); sending the agent there is not.
DIRECTIVE_RE = re.compile(r"\b(see|read|refer|consult|as per|in)\b", re.I)
DIRECTIVE_WINDOW = 25

# Flags per file per metric before the rest are summarised.
SHOWN_PER_FILE = 3

OVERRIDE_RE = re.compile(r"<!--\s*hygiene-ok:\s*([a-z_]+)\s*(?:—|--)?\s*(.*?)-->", re.S)
LIST_ITEM_RE = re.compile(r"^\s*([-*]|\d+\.)\s")

# A marker is metadata, not instruction. Measured as prose, writing one to excuse a
# flag raises a different flag, which makes the override mechanism self-defeating.
# Override detection reads the raw file, so stripping here does not hide markers.
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)

# Markup is not prose. A bold lead-in label ("**Rule.** Detail ...") must not fuse
# with the sentence after it, and a list marker is neither a word nor a sentence.
EMPHASIS_RE = re.compile(r"\*\*")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[\"A-Z(])")


@dataclasses.dataclass(frozen=True)
class Flag:
    """A single threshold breach, addressed to one file."""

    path: str
    metric: str
    value: int
    limit: int
    detail: str


def load_thresholds(doc: pathlib.Path) -> dict[str, int]:
    """Parse the ``thresholds`` fenced block out of the shared hygiene doc."""
    if not doc.is_file():
        raise FileNotFoundError(f"thresholds live in {doc}, which is missing")
    block = re.search(r"```thresholds\n(.*?)```", doc.read_text(), re.S)
    if block is None:
        raise ValueError(f"no ```thresholds block in {doc}")
    values = {
        key.strip(): int(raw.split("#")[0])
        for key, raw in re.findall(r"^(\w+)\s*=\s*(.+)$", block.group(1), re.M)
    }
    if not values:
        raise ValueError(f"```thresholds block in {doc} parsed to nothing")
    return values


def discover(root: pathlib.Path) -> list[pathlib.Path]:
    """Every instruction file in scope, in a stable order."""
    found = sorted(root.glob("skills/*/SKILL.md")) + sorted(root.glob("agents/*/agent.md"))
    found += sorted(root.glob("shared/*.md")) + [root / "CLAUDE.md"]
    return [p for p in found if p.is_file()]


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter, body); frontmatter is empty when absent."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 3)
    if end == -1:
        return "", text
    return text[4:end], text[end + 5 :]


def strip_code(text: str) -> str:
    """Drop fenced blocks and HTML comments; reduce inline spans to a single token."""
    text = re.sub(r"^\s*```.*?^\s*```", "", text, flags=re.S | re.M)
    text = COMMENT_RE.sub("", text)
    return re.sub(r"`[^`]*`", "X", text)


def blocks(body: str) -> list[str]:
    """Top-level list items and standalone paragraphs, code fences dropped."""
    out: list[str] = []
    current: list[str] = []
    in_fence = False
    for line in body.split("\n"):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if LIST_ITEM_RE.match(line):
            if current:
                out.append("\n".join(current))
            current = [line]
        elif not line.strip() or line.startswith("#"):
            if current:
                out.append("\n".join(current))
            current = []
        else:
            current.append(line)
    if current:
        out.append("\n".join(current))
    return out


def sentences(block: str) -> list[str]:
    """Sentences within a block, treating each nested list line as its own."""
    found: list[str] = []
    for line in block.split("\n"):
        text = EMPHASIS_RE.sub("", LIST_ITEM_RE.sub("", strip_code(line))).strip()
        if text:
            found.extend(s for s in SENTENCE_SPLIT_RE.split(text) if s)
    return found


def overrides(text: str) -> set[str]:
    """Metric names this file has an acknowledged exception for."""
    return {metric for metric, _ in OVERRIDE_RE.findall(text)}


def check_file(path: pathlib.Path, root: pathlib.Path, limits: dict[str, int]) -> list[Flag]:
    """Every per-file threshold breach, minus acknowledged overrides."""
    raw = path.read_text()
    frontmatter, body = split_frontmatter(raw)
    name = relative(path, root)
    excused = overrides(raw)
    found: list[Flag] = []

    body_words = len(strip_code(body).split())
    if body_words > limits["file_max_words"] and "file_max_words" not in excused:
        found.append(Flag(name, "file_max_words", body_words, limits["file_max_words"], ""))

    described = re.search(r"^description:(.*?)(?=^\w+:|\Z)", frontmatter, re.S | re.M)
    if described:
        count = len(described.group(1).split())
        limit = limits["description_max_words"]
        if count > limit and "description_max_words" not in excused:
            found.append(Flag(name, "description_max_words", count, limit, "advisory"))

    parsed = blocks(body)
    for block in parsed:
        words = len(strip_code(block).split())
        if words > limits["block_max_words"] and "block_max_words" not in excused:
            found.append(
                Flag(name, "block_max_words", words, limits["block_max_words"], summarise(block))
            )
        for sentence in sentences(block):
            words = len(sentence.split())
            if words > limits["sentence_max_words"] and "sentence_max_words" not in excused:
                found.append(
                    Flag(
                        name,
                        "sentence_max_words",
                        words,
                        limits["sentence_max_words"],
                        summarise(sentence),
                    )
                )

    non_negotiables = len(re.findall(r"\*\*Non-negotiable:", body))
    if parsed:
        density = round(100 * non_negotiables / len(parsed))
        limit = limits["nonneg_max_density_pct"]
        if density > limit and "nonneg_max_density_pct" not in excused:
            found.append(
                Flag(name, "nonneg_max_density_pct", density, limit, f"{non_negotiables}/{len(parsed)} blocks")
            )
    return found


def summarise(text: str, width: int = 64) -> str:
    """One-line preview of a block or sentence."""
    return re.sub(r"\s+", " ", strip_code(text).strip())[:width]


def check_references(paths: list[pathlib.Path], root: pathlib.Path) -> list[Flag]:
    """Dangling file references, and runtime files pointing at non-runtime docs."""
    found: list[Flag] = []
    for path in paths:
        name = relative(path, root)
        text = path.read_text()
        for target in set(re.findall(r"`([A-Za-z0-9_./-]+\.md)`", text)):
            if target in PROJECT_LOCAL_DOCS or "<" in target:
                continue
            resolved = (root / target).is_file() or any(root.glob(f"**/{target}"))
            if not resolved and "former" not in text[: text.find(target)][-90:]:
                found.append(Flag(name, "dangling_reference", 0, 0, target))
        # This doc defines the metric, so it has to name the anti-pattern.
        if path.samefile(root / THRESHOLDS_DOC):
            continue
        # Fenced blocks may hold text destined for another repo, not instructions here.
        prose = re.sub(r"^\s*```.*?^\s*```", "", text, flags=re.S | re.M)
        for doc in NON_RUNTIME_DOCS:
            for match in re.finditer(re.escape(doc), prose):
                window = prose[max(0, match.start() - DIRECTIVE_WINDOW) : match.start()]
                if DIRECTIVE_RE.search(window):
                    found.append(Flag(name, "runtime_reachability", 0, 0, doc))
    return found


def relative(path: pathlib.Path, root: pathlib.Path) -> str:
    """Repo-relative path, so output is readable and pasteable."""
    return str(path.relative_to(root))


def check_duplication(paths: list[pathlib.Path], root: pathlib.Path, size: int = 8) -> list[Flag]:
    """Prose shared by two or more files. Candidates only — citations repeat legitimately."""
    seen: dict[str, set[str]] = {}
    for path in paths:
        _, body = split_frontmatter(path.read_text())
        tokens = re.findall(r"[a-z]+", strip_code(body).lower())
        for start in range(len(tokens) - size):
            seen.setdefault(" ".join(tokens[start : start + size]), set()).add(relative(path, root))

    # Overlapping n-grams describe one passage, so report per file-set, not per gram.
    shared: dict[str, list[str]] = {}
    for gram, files in sorted(seen.items()):
        if len(files) > 1:
            shared.setdefault(", ".join(sorted(files)), []).append(gram)
    return [
        Flag(pair, "duplication", len(grams), 1, f"{grams[0]} ...")
        for pair, grams in sorted(shared.items())
    ]


def count_instructions(paths: list[pathlib.Path]) -> int:
    """Discrete rules an agent could be asked to hold at once."""
    total = 0
    for path in paths:
        _, body = split_frontmatter(path.read_text())
        total += sum(1 for line in strip_code(body).split("\n") if LIST_ITEM_RE.match(line))
    return total


def report(flags: list[Flag], instructions: int, override_count: int, limits: dict[str, int]) -> None:
    """Print flags grouped by metric, then the corpus-wide advisories."""
    if not flags:
        print("No flags.")
    for metric in sorted({flag.metric for flag in flags}):
        matching = [flag for flag in flags if flag.metric == metric]
        print(f"\n{metric}  ({len(matching)})")
        for path in sorted({flag.path for flag in matching}):
            in_file = [flag for flag in matching if flag.path == path]
            for flag in in_file[:SHOWN_PER_FILE]:
                measured = f"{flag.value}>{flag.limit}" if flag.limit else ""
                print(f"  {flag.path:<38} {measured:>8}  {flag.detail}")
            if len(in_file) > SHOWN_PER_FILE:
                print(f"  {'':<38} {'':>8}  ... and {len(in_file) - SHOWN_PER_FILE} more")
    print(f"\ninstruction_count  {instructions} (soft {limits['instruction_count_soft']}, advisory trend)")
    print(f"overrides          {override_count} (max {limits['max_overrides']})")


def main() -> int:
    """Measure every in-scope file and print the report."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    root = pathlib.Path.cwd()
    limits = load_thresholds(root / THRESHOLDS_DOC)
    paths = discover(root)
    if not paths:
        raise FileNotFoundError(f"no instruction files found under {root}")
    LOGGER.info("Checked %d files against %s", len(paths), THRESHOLDS_DOC)

    flags = [flag for path in paths for flag in check_file(path, root, limits)]
    flags += check_references(paths, root)
    flags += check_duplication(paths, root)
    override_count = sum(len(overrides(path.read_text())) for path in paths)
    report(flags, count_instructions(paths), override_count, limits)
    return 0


if __name__ == "__main__":
    sys.exit(main())
