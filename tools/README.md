# tools — sources & derivations

Where the numbers in `shared/instruction-hygiene.md` came from. Not loaded at runtime; the thresholds themselves live in that file, and this one explains them so they aren't voodoo constants.

## Method

Two bases, and the difference matters when a threshold is challenged:

- **Derived** — the threshold sits in a real gap in this repo's own distribution, so it names an outlier rather than a preference. Re-derive it if the corpus changes shape.
- **Conventional** — a round number chosen for headroom. Weaker. Say so rather than defending it as evidence.

The distributions cited below are dated evidence for a threshold, not a status report — run the check for where the corpus sits now. Any sentence figure recorded before 2026-07-30 reads high: until then the splitter fused a bold lead-in label into the sentence following it and counted a list marker as a word, so a re-derivation of `sentence_max_words` should not reuse those numbers.

## Per threshold

| threshold | basis | derivation |
| --- | --- | --- |
| `sentence_max_words = 25` | external | Plain-language consensus: average 15–20, maximum 25. Adopted wholesale: this repo's own mean and median sat inside that band when it was set, so the number is the external convention rather than a local gap. |
| `block_max_words = 65` | derived | Blocks cluster at 59, 61, 62, 63, 64 across four independently-written files, then jump 17 words to 81. Four files converging in a 5-word band reads as a natural ceiling for one rule plus its justification. |
| `nonneg_max_density_pct = 25` | derived | Densities run 0, 0, 0, 13, 14, 18, 19, then 38 — a 19-point gap, the cleanest break in the corpus. |
| `file_max_words = 800` | conventional | No break in the distribution (138…683, 729). Backstop against a future doubling. Anthropic's own limit is 500 lines, roughly 7x looser than this. |
| `description_max_words = 60` | derived, advisory | Gap between 55 and 70. Advisory because Anthropic's guidance pushes the other way: descriptions do trigger discrimination, the platform allows 1,024 characters, and cutting trigger terms makes a skill fire less. |
| `instruction_count_soft = 150` | external, advisory | IFScale's degradation onset. Advisory only — see the caveat below. |
| `max_overrides = 6` | conventional | Enough for genuine exceptions, few enough that a seventh means the threshold is wrong. |

Two candidate metrics were considered and dropped: **non-negotiables per file** (counts run 0…4 with no gap, and its only finding was a false positive) and **bullets per file/section** (no failure mode the size and block metrics don't already cover).

## What the external evidence does and doesn't support

Measured against published guidance this repo is comfortably inside every limit — about 7x inside Anthropic's SKILL.md length, a tenth of `claudelint`'s `CLAUDE.md` cap, and roughly 60% of the instruction-density onset. These thresholds are therefore **house style preserving headroom, not protection from a nearby cliff**. The defects worth catching are the structural ones external guidance doesn't quantify: duplication, enumeration, dangling references.

The IFScale caveat: it is an unreviewed arXiv preprint, and its "instructions" are keyword-inclusion demands, a much cruder unit than a prose guidance rule. Whether that degradation curve predicts this one is an assumption the paper does not test. It supports the shape of the claim — more rules cost something, and for Claude models the cost is linear from the first rule rather than starting after a free allowance — but 150 is not a number to treat as precise. Hence advisory.

## Sources

- [Anthropic — Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md) — 500-line SKILL.md guidance, 1,024-character description limit, progressive disclosure, one-level-deep references, consistent terminology.
- [Jaroslawicz et al., *How Many Instructions Can LLMs Follow at Once?* (arXiv 2507.11538)](https://arxiv.org/pdf/2507.11538) — the IFScale benchmark; degradation onset and per-model decay shapes.
- [`claudelint` — `claude-md-size`](https://claudelint.com/rules/claude-md/claude-md-size) — 40KB default, matching Claude Code's own warning threshold.
- [HumanLayer — Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — community consensus on `CLAUDE.md` length and the ~50-instruction system-prompt baseline.
- [Readability Guidelines — Sentence length](http://readabilityguidelines.wikidot.com/sentence-length), [Federal Plain Language Guidelines](https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf), [Australian Style Manual — Sentence length](https://www.stylemanual.gov.au/style-manual-resources/government-writing-handbook/editors-tips/sentence-length) — the 15–20 average, 25 maximum convergence.

## Tests

`python3 -m unittest discover -s tools` — stdlib `unittest`, no dependencies. The suite covers the parsing and threshold logic: `strip_code`, `split_frontmatter`, `blocks`, `sentences`, `overrides`, `load_thresholds`, `check_file`, `count_instructions`, `summarise`.

`check_references` and `check_duplication` are not covered — they need fixture repo trees, and both were hand-verified against this repo's own content when introduced. Tests that could not be written red-first were each confirmed by mutating the implementation and watching them fail, per `skills/coding-standards`.
