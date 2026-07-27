# Agentic engineering topics to explore

## Proposed instruction edits — drafted, awaiting sign-off

Concrete edits to existing instruction files, each drafted with its evidence and ready to review. Unlike the topics below these need a decision rather than exploration — delete an item once its edit has landed or been rejected. All three came from `f1_fantasy`'s `fastf1_v1` effort (2026-07-27) via the split-authority handoff; line references are to that repo's `docs/fastf1_v1/log.md` at commit `95c6bc0`.

### A. `skills/coding-standards/SKILL.md` — when red-first is impossible, verify by mutation

**Gap:** the Testing section covers *watch it fail for the reason you expect* and *an unexpected pass is a defect in the test*. It has no answer for red-first being structurally **impossible** — a test that cannot fail before the implementation exists because what it asserts is vacuously true beforehand.

**Drafted text** — insert after the "unexpected pass is a defect" bullet:

- **When red-first is impossible, verify by mutation.** Some tests cannot fail before the implementation exists — an assertion that nothing was cached passes vacuously when no caching code exists at all, and a new function's first red is an `ImportError` that demonstrates nothing about behaviour. **Non-negotiable:** a test that could not be observed failing for the right reason must instead be confirmed by deliberately breaking the finished implementation — drop the guard, shift the boundary, reinline the duplicate — and watching it go red; name the mutation and quote the failure when reporting. The same applies to a pure refactor, which adds no behaviour to test: if mutating the code you just consolidated leaves the suite green, the refactor is unprotected and that coverage gap is itself the finding.

**Evidence** — four independent instances: `log.md:317` (an "empty schedule is not cached" assertion would have passed vacuously pre-implementation, so it was verified by dropping the `not schedule.empty` guard instead); `log.md:364` (first red was signature-level `TypeError`/`ImportError`, so all three assertions were confirmed by mutation); `log.md:284` (two metrics tests first went red on a `KeyError` about `METRIC_WEIGHTS` itself, so the dict assertions were moved after the behavioural ones); and the rolling-window helper dedup, where mutating the consolidated helper left every output test green, revealing the refactor was unprotected. Currently captured only in `f1_fantasy`'s per-project memory, so no other project benefits — the main argument for promoting it.

**Overlap to resolve before applying:** the drafted `ImportError` example restates a clause already in `SKILL.md:38`. More importantly `SKILL.md:39` frames *any* unexpected pass as a defect in the test and already prescribes a mutation ("back it out, confirm the test fails, then restore"), so appending this bullet as-is would leave the two contradicting each other — 39 wants narrowing to "passes because it exercises a different path" so this bullet can own "passes because the assertion is vacuously true beforehand".

### B. `shared/persistent-docs.md` — annotate superseded content in place

**Gap:** the file defines the structure (`BACKLOG.md`, `docs/<effort-name>/`) but says nothing about how content ages, so a fresh session would reasonably just rewrite or delete a line that has stopped being true.

**Drafted text** — add as a fourth bullet:

- **Superseded content is annotated in place, not rewritten or deleted** — a requirement or plan step that stops being true keeps its original wording and gains a dated marker beside it (inline `[Superseded YYYY-MM-DD: …]` for a sentence, a blockquote for a whole step), so the effort's history stays readable and a reader can see what was believed when. This includes lists of files an effort touched: a file deleted during the effort stays listed, marked with its deletion date and a recovery SHA, rather than dropped. `log.md` is append-only by nature — correct it with a new entry, never by editing an old one.

**Evidence** — the convention was applied five times before being stated: `requirements.md:5` (`[Superseded 2026-07-25: external_data has been removed from the repo — see log.md.]`), `plan.md:5` and `plan.md:9` (blockquote `> **Superseded YYYY-MM-DD:**` banners for whole steps), `log.md:97` (inline marker on an earlier claim), and `log.md:101`, which states the reasoning directly — the originals keep their wording "so the effort's history stays readable without implying the module still exists". Alex then stated it explicitly on 2026-07-27, on a review finding that `plan.md`'s "Relevant files" listed five files deleted during the effort: *"indicate in the documentation that these files were deleted during this effort, leaving the filenames in the plan"* — confirming that keeping the filenames was the point, not merely marking them.

**Overlap:** none. `persistent-docs.md` is purely structural today, and both `CONVENTIONS.md`'s "Persistent documents in project repos" section and the `init-project-docs` skill defer the mechanics to it, so this lands in one place and needs no follow-on edits. Style matches the existing bullets. Alex chose to route it through here rather than apply it directly, so it still wants a sign-off pass.

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

**Status**: queued, not started

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger
- Review the skills built in this repo against what already exists — Claude Code's built-in skills/commands, Anthropic's published skills, and skills shared across the broader internet — to spot overlap, gaps, and ideas worth borrowing. Approach TBD (how to discover and compare against external skill sets isn't figured out yet).
