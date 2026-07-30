# Instruction hygiene

Standing checks on instruction content: `skills/*/SKILL.md`, `agents/*/agent.md`, `shared/*.md`, skill frontmatter `description`s, and each repo's `CLAUDE.md`. Project-local docs (`BACKLOG.md`, `docs/<effort-name>/*.md`) are out of scope — they grow by design as work proceeds.

These are house-style limits that preserve headroom, not safety limits. Measured against published guidance, this content sits far inside where models actually degrade. A flag means "look at this", never "this is broken", and **a flag never blocks a change**. Derivations and sources are in `agentic`'s `tools/README.md` — not needed to apply the rules.

## Thresholds

```thresholds
sentence_max_words     = 25
block_max_words        = 65
nonneg_max_density_pct = 25
file_max_words         = 800
description_max_words  = 60
instruction_count_soft = 150
max_overrides          = 6
```

Four defects have no threshold — any occurrence is a finding:

- the same rule stated in two files (`duplication`);
- a reference to a file or section that doesn't exist (`dangling_reference`);
- a runtime-loaded file directing a read of one that isn't (`runtime_reachability`, currently only `learning/CONVENTIONS.md` and `learning/INBOX.md`);
- a file inline-enumerating another file's contents — **no check implements this one**; it is caught by reading, not by running the tool.

Run `python3 tools/instruction_hygiene.py` from the repo root.

## Responding to a flag

- **A long block or sentence gets split or promoted, not compressed.** A rule is often long because it carries a non-negotiable plus the boundary that makes it applicable. Give it sub-bullets or its own section. Cutting words to reach a number loses the rule and keeps the score.
- **Duplication flags are candidates, not verdicts.** Repeated *citation* phrasing across files is the consistency convention working correctly. Only repeated *rule content* is a defect, and separating the two needs a human.
- **A long `description` matters only if it is also vague.** Descriptions do trigger discrimination, and cutting trigger terms makes a skill fire less often. Prefer specificity over brevity here, and treat the word count as advisory.
- **A rising instruction count is a trend, not a limit.** The 150 figure comes from a keyword-inclusion benchmark, which is a crude proxy for prose guidance. Watch the direction of travel; don't treat the number as precise.

## Overriding a threshold

Mark a deliberate exception beside the text it excuses:

`<!-- hygiene-ok: <metric> — <reason>. <YYYY-MM-DD> -->`

An override is file-wide for its metric, not scoped to the text beside it. One `sentence_max_words` marker silences every long sentence in that file, including ones written later — so use them sparingly, and prefer splitting.

These markers are metadata, not instruction. Frontmatter cannot hold one, so put a `description` override in the body just below the closing `---`. The check counts overrides as their own metric: past `max_overrides`, the threshold is wrong rather than the content.
