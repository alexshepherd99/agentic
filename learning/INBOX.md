# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

### Topic: Define size and structure metrics for instruction content

Cheap standing checks — in the spirit of `CLAUDE.md`'s ~1,500-word knowledge-base cap — run after every update to instruction content, flagging sprawl and drift before they dilute the instructions. The failure mode is silent: a bloated or mushy skill doesn't fail visibly, it just stops being followed, and its instructions are the first thing dropped in a long session.

**Scope**: everything this repo ports into project repos (`skills/*/SKILL.md`, `agents/*/agent.md`, `shared/*.md`); each repo's `CLAUDE.md`, always loaded and so the most expensive place for bloat; and skill frontmatter `description`s tracked as their own metric — every description is loaded every session whether or not its skill fires, making them the highest-leverage words in the repo. Project-local docs (`BACKLOG.md`, `docs/<effort-name>/*.md`) are deliberately out of scope: they grow by design as work proceeds, so a cap there would be actively wrong.

**Size alone is the wrong measure** — the 2026-07-28 baseline says so. No file is within half the existing 1,500-word cap (largest is `onboard-project` at 905), yet two structural signals are already degrading: longest single bullets have reached 136 words (`collaboration-workflow`) and 122 (`coding-standards`), no longer scannable as rules; and non-negotiable density is 3-of-7 bullets in `collaboration-workflow` against 3-of-23 in `coding-standards`, where the standing rule is that the label is used sparingly. Frontmatter descriptions run 38–79 words.

**Candidate metrics to decide on**: per-file word count, capped well below 1,500; longest single bullet; non-negotiable count and density; frontmatter description length; bullets per file and per section; cross-file duplication of the same rule.

**Home**: a new `shared/` file (say `instruction-hygiene.md`), so thresholds load at runtime in both this repo and project repos, referenced from `CLAUDE.md` and the review skill — matching how `collaboration-workflow.md` and `persistent-docs.md` already work. Not `CONVENTIONS.md`, which isn't loaded at skill runtime, so an agent editing a skill wouldn't have the thresholds to hand.

**Open questions**: whether "after every update" means a step in the end-of-session review or a real hook; whether a tripped threshold only ever flags and never blocks (cf. the review skill's report-only rule); and how a threshold gets deliberately overridden without the metric decaying into noise.

**Status**: queued, not started — top of the queue.

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
- Revisit `INBOX.md`'s own conventions. Its title ("topics to explore") doesn't cover drafted, ready-to-apply edits, and parking three of them here in 2026-07 pushed the file past `CLAUDE.md`'s ~1,500-word cap purely on entries designed to be deleted as soon as they landed (they did, on 2026-07-28, taking it back to ~850). Decide whether long drafted text belongs somewhere else entirely — say `proposals/`, one file per proposal — with the INBOX holding only a pointer. The related question of whether a word cap on a queue measures anything useful now sits with the metrics topic above.

## Considered and deliberately not proposed

Surfaced by `f1_fantasy`'s `fastf1_v1` handoff (2026-07-27) alongside the three instruction edits that landed, but judged not worth promoting. Kept so the same observations don't get re-raised from scratch; line references are to that repo's `docs/fastf1_v1/log.md` at commit `95c6bc0`.

- **Check third-party assumptions against reality before writing code** — the FastF1 `EventSchedule` pickle round-trip check (`log.md:309-313`) and the selective-session-load equivalence check (`log.md:113`) both de-risked a change before any code was written. Real, but reads as ordinary care rather than a rule that would change an agent's behaviour.
- **An entrypoint no test exercises will drift silently** — `log.md:371-384`, on deleting `scripts/get_fastf1_data.py` after it drifted twice without a red test. Already captured concretely in `f1_fantasy`'s `BACKLOG.md` ("No test exercises any script's `__main__` block"), which exists to decide the standard; generalising it now would pre-empt that decision.
