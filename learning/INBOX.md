# Agentic engineering topics to explore

## Proposed instruction edits — drafted, awaiting sign-off

Concrete edits to existing instruction files, each drafted with its evidence and ready to review. Unlike the topics below these need a decision rather than exploration — delete an item once its edit has landed or been rejected. All three came from `f1_fantasy`'s `fastf1_v1` effort (2026-07-27) via the split-authority handoff; line references are to that repo's `docs/fastf1_v1/log.md` at commit `95c6bc0`.

### C. `shared/collaboration-workflow.md` — don't let a measurement claim more than it can carry

**Gap:** nothing in this repo covers evidence strength. The `how-we-work` skill covers *say what failed and how*; neither file covers *say what the numbers cannot tell you*.

**Drafted text** — add as a seventh bullet:

- **Don't let a measurement claim more than it can carry.** When a change is justified by numbers, state what the comparison can and cannot distinguish before stating what it shows — a delta smaller than its own run-to-run spread is not evidence, and a handful of races, runs or trials usually cannot separate the options being weighed. **Non-negotiable:** a change that measured neutral is written up as neutral; "no measurable cost" is not "an improvement", and the correctness or simplicity argument for it has to stand on its own.

**Evidence** — two strong instances: `log.md:168`, on choosing an indicator weight ("At nine races, one season and a single bookmaker snapshot, that cannot distinguish 1x from 2x from 3x. 2x is a judgement call."), and `log.md:260,272`, after a table showing every delta inside its own race-to-race spread ("none is distinguishable from noise at ten races… So this is a simplification at no measurable cost, not an accuracy improvement, **and it should not be written up as one.**").

**Overlap:** none — a grep for `supersed|mutat|noise|measur|spread` across the repo turns up nothing on this. Worth deciding whether the home is `collaboration-workflow.md` (how work is reported, applies to both this repo and project repos) or `coding-standards`; the drafted bullet assumes the former.

### Considered and deliberately not proposed

- **Check third-party assumptions against reality before writing code** — the FastF1 `EventSchedule` pickle round-trip check (`log.md:309-313`) and the selective-session-load equivalence check (`log.md:113`) both de-risked a change before any code was written. Real, but reads as ordinary care rather than a rule that would change an agent's behaviour.
- **An entrypoint no test exercises will drift silently** — `log.md:371-384`, on deleting `scripts/get_fastf1_data.py` after it drifted twice without a red test. Already captured concretely in `f1_fantasy`'s `BACKLOG.md` ("No test exercises any script's `__main__` block"), which exists to decide the standard; generalising it now would pre-empt that decision.

## Immediate — needed to start using skills on future projects

### Topic: Build a manually-run repo-review skill

Turn the periodic repo review (done manually this session) into a reusable, manually-invoked skill, usable both in this repo and in project repos (mounted via the standard share). It should audit the repo for gaps, inconsistencies, drift / stale cross-references, duplication, and sprawl, and surface suggestions for the human to weigh — report/propose only, never act without sign-off (cf. `init-project-docs`).

Keep it open-ended, not a fixed checklist: the agent should recommend what's worth reviewing based on what it actually finds, rather than mechanically walking a prescriptive list. A short set of standing prompts (sprawl caps, dangling references, duplication, docs-vs-reality drift) can seed it, but the agent should stay free to raise anything else it notices.

Validated by the one-off full-repo pass (2026-07): stale cross-references (a doc pointing elsewhere for content that isn't there), structure/overview docs missing a folder that exists, entry/front-door docs that never state what the thing is, the same discipline duplicated across an always-loaded doc and a skill, and unclear relationships between adjacent sibling sections.

One concrete instance of the "introspection process for gradually improving the repo" item under Longer-term below.

Adjacent mode to scope in or out: checking an *incoming* proposal against what its target file already says, rather than auditing the repo as-is. The `fastf1_v1` handoff needed exactly that — three drafted bullets, one of which duplicated a clause and contradicted a rule in the very file it targeted.

**Status**: queued, not started

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger. Datapoint (`fastf1_v1`, 2026-07-27): three instruction proposals surfaced from a scheduled end-of-effort consistency review, not noticed in passing — and one of them had been sitting in that project's per-project memory the whole time, where no other project could benefit from it. Suggests the trigger wants to be an explicit step in an effort's plan, and that it should include sweeping per-project memories for anything general enough to promote.
- Review the skills built in this repo against what already exists — Claude Code's built-in skills/commands, Anthropic's published skills, and skills shared across the broader internet — to spot overlap, gaps, and ideas worth borrowing. Approach TBD (how to discover and compare against external skill sets isn't figured out yet).
- Give the split-authority handoff a defined shape. `CONVENTIONS.md`'s split-authority note says only "hand text across manually", which undersells what actually works: the project session writes a structured proposals file (per proposal — the gap, evidence as `file:line` pointers, drop-in text, suggested placement) and the `agentic` session verifies and places it. Validated by the `fastf1_v1` handoff on 2026-07-27 (three proposals). The load-bearing half is the receiving end: a project session cannot read the target files, so it structurally cannot tell whether its drafted text is already covered — the `agentic` session must always run that check before applying, and on this occasion it caught a proposal that would have left a skill contradicting itself. Open question: whether this is enough procedure to deserve a skill, or just a few sentences added to `CONVENTIONS.md`'s split-authority section.
- Revisit `INBOX.md`'s own conventions. The file has outgrown two of them: its title ("topics to explore") doesn't cover drafted, ready-to-apply edits, and it tripped `CLAUDE.md`'s ~1,500-word sprawl cap purely from three entries designed to be deleted as soon as they land. A word cap on a queue measures throughput, not sprawl — decide whether the cap should exclude transient sections, or whether long drafted text belongs somewhere else entirely (say `proposals/`, one file per proposal) with the INBOX holding only a pointer.
