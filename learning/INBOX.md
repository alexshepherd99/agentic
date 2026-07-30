# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

### Topic: Define size and structure metrics for instruction content

**Status**: settled and running, 2026-07-29 to 2026-07-30. `shared/instruction-hygiene.md` holds the thresholds and triage rules, `tools/instruction_hygiene.py` computes them with a stdlib `unittest` suite beside it, and `tools/README.md` records every derivation and source. Runs as an end-of-session step in `agentic` only, prints a one-line outcome, and flags but never blocks. How it got here is in the commits; what follows is what is still open.

Two decisions worth not re-deriving. `CONVENTIONS.md` gets no entry for this — the thresholds and their rationale already live in the two files above. And the one standing `duplication` flag, the citation of `shared/persistent-docs.md` shared by `grill-me` and `init-project-docs`, stays exactly as it is: verified benign (the consistency convention working correctly), not overridden because a `duplication` override is file-wide and would blind both files to real duplication later, and not silenced by raising the n-gram size from 8 to 11 — the corpus's longest shared run is 10 tokens, so with one data point there is no distribution to derive from and 11 would simply be fitted to it. Confirmed 2026-07-30; don't re-propose either.

Remaining:

- **Two metrics move mechanically under splitting** — the prescribed fix for a long block is to split it into bullets, and `count_instructions` counts every bullet, so this triage moved `instruction_count` 73 → 98 (+34%) while clearing 7 block flags. `nonneg_max_density_pct` is the mirror case: a ratio whose denominator is the block count, so any split lowers it regardless of content — it cleared here purely as a side effect. Both need a different unit, or an explicit note that they track splitting rather than quality.
- **The em dash counts as a word** — `" — ".split()` yields `"—"`. Same family as the label-fusion and list-marker defects fixed earlier on 2026-07-30. Largely defused by the move to 42: it no longer decides any flag. It does still inflate every count by one per dash, and the 41 → 46 gap the threshold was derived from would shift slightly if fixed, so re-derive rather than just patching the tokenizer.
- **Nothing implements the enumeration check** — the shared doc listed four zero-tolerance defects, but only `duplication`, `dangling_reference` and `runtime_reachability` exist. The four enumerating files found on 2026-07-29 were found by hand. The doc now states the gap; decide whether to build the check or drop the claim.
- **Decide whether a block should count its list marker** — `sentence_max_words` now ignores `- `, `block_max_words` still counts it, so the same text is measured two ways. Changing it shifts every list block by one word, which means revisiting the derivation (cluster 59–64, jump to 81) rather than just the code.
- **Make the check runnable from a project repo** — it resolves thresholds relative to the repo root, so a project session can't run it against its own `CLAUDE.md`. Until then the end-of-session step sits only in `agentic`'s `CLAUDE.md`, not the shared workflow.

### Topic: Give the split-authority handoff a defined shape

`CONVENTIONS.md`'s split-authority note says only "hand text across manually", which undersells what actually works: the project session writes a structured proposals file (per proposal — the gap, evidence as `file:line` pointers, drop-in text, suggested placement) and the `agentic` session verifies and places it. Validated by the `fastf1_v1` handoff on 2026-07-27 (three proposals).

The load-bearing half is the receiving end: a project session cannot read the target files, so it structurally cannot tell whether its drafted text is already covered — the `agentic` session must always run that check before applying. Both handoffs bear this out. It caught a proposal that duplicated a clause and contradicted a rule in the very file it targeted, and applying it on 2026-07-28 required reshaping that proposal into two edits (narrowing the rule it contradicted) rather than the single append it was written as — a change no project session could have known to make.

Open question: whether this is enough procedure to deserve a skill, or just a few sentences added to `CONVENTIONS.md`'s split-authority section.

**Status**: queued, not started. Sequenced before the repo-review skill below, whose "adjacent mode" — checking an incoming proposal against its target — is exactly this check; deciding the handoff's shape first settles whether that skill absorbs it or defers to it.

### Topic: Build a manually-run repo-review skill

Turn the periodic repo review (done manually as a one-off in 2026-07) into a reusable, manually-invoked skill, usable both in this repo and in project repos (mounted via the standard share). It should audit the repo for gaps, inconsistencies, drift / stale cross-references, duplication, and sprawl, and surface suggestions for the human to weigh — report/propose only, never act without sign-off (cf. `init-project-docs`).

Keep it open-ended, not a fixed checklist: the agent should recommend what's worth reviewing based on what it actually finds, rather than mechanically walking a prescriptive list. A short set of standing prompts (sprawl caps, dangling references, duplication, docs-vs-reality drift) can seed it, but the agent should stay free to raise anything else it notices.

Validated by the one-off full-repo pass (2026-07): stale cross-references (a doc pointing elsewhere for content that isn't there), structure/overview docs missing a folder that exists, entry/front-door docs that never state what the thing is, the same discipline duplicated across an always-loaded doc and a skill, and unclear relationships between adjacent sibling sections.

One concrete instance of the "introspection process for gradually improving the repo" item under Longer-term below.

Adjacent mode to scope in or out: checking an *incoming* proposal against what its target file already says, rather than auditing the repo as-is. The `fastf1_v1` handoff needed exactly that — three drafted bullets, one of which duplicated a clause and contradicted a rule in the very file it targeted. Settled by the split-authority item above, which owns that check; scope it in here only if that item lands as prose rather than a skill.

Consumes the metrics item above: those thresholds are this skill's concrete seed checks, and the open-ended judgment pass is what this skill adds on top.

**Status**: queued, not started

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger. Datapoint (`fastf1_v1`, 2026-07-27): three instruction proposals surfaced from a scheduled end-of-effort consistency review, not noticed in passing — and one of them had been sitting in that project's per-project memory the whole time, where no other project could benefit from it. Suggests the trigger wants to be an explicit step in an effort's plan, and that it should include sweeping per-project memories for anything general enough to promote.
- Review the skills built in this repo against what already exists — Claude Code's built-in skills/commands, Anthropic's published skills, and skills shared across the broader internet — to spot overlap, gaps, and ideas worth borrowing. Approach TBD (how to discover and compare against external skill sets isn't figured out yet).
- Revisit `INBOX.md`'s own conventions. Its title ("topics to explore") doesn't cover drafted, ready-to-apply edits, and parking three of them here in 2026-07 pushed the file past `CLAUDE.md`'s ~1,500-word cap purely on entries designed to be deleted as soon as they landed (they did, on 2026-07-28, taking it back to ~850). Decide whether long drafted text belongs somewhere else entirely — say `proposals/`, one file per proposal — with the INBOX holding only a pointer. The related question of whether a word cap on a queue measures anything useful was settled 2026-07-29: queue and project-local docs are out of scope for the hygiene metrics, so this file has no cap.

## Considered and deliberately not proposed

Surfaced by `f1_fantasy`'s `fastf1_v1` handoff (2026-07-27) alongside the three instruction edits that landed, but judged not worth promoting. Kept so the same observations don't get re-raised from scratch; line references are to that repo's `docs/fastf1_v1/log.md` at commit `95c6bc0`.

- **Check third-party assumptions against reality before writing code** — the FastF1 `EventSchedule` pickle round-trip check (`log.md:309-313`) and the selective-session-load equivalence check (`log.md:113`) both de-risked a change before any code was written. Real, but reads as ordinary care rather than a rule that would change an agent's behaviour.
- **An entrypoint no test exercises will drift silently** — `log.md:371-384`, on deleting `scripts/get_fastf1_data.py` after it drifted twice without a red test. Already captured concretely in `f1_fantasy`'s `BACKLOG.md` ("No test exercises any script's `__main__` block"), which exists to decide the standard; generalising it now would pre-empt that decision.
