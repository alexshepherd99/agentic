# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

### Topic: Final full-repo review (folds in the duplication sweep)

A comprehensive, one-time review of *everything* in this repo — not just duplication — inviting suggestions, changes, and fixes. Walk area by area (`CLAUDE.md`, `learning/`, `agents/`, `skills/`, `shared/`, all READMEs, the symlink setup) and surface anything worth improving: gaps, inconsistencies, drift / stale cross-references, duplication (the learning-vs-skills sweep is folded in here and re-checked fresh), unclear or overlong instructions, sprawl, naming, structure.

**Ask plenty of questions.** This review should be conversational and question-heavy — check assumptions and preferences rather than unilaterally proposing fixes. Report/propose only; get sign-off before changing anything (cf. `init-project-docs` and the working conventions in `CLAUDE.md`).

Best done *after* the other Immediate items land, since it reviews their outputs too. Kept separate from the "manually-run repo-review skill" topic below: this is a one-off pass over *this* repo. As it runs, propose additions/refinements to fold into that skill-building topic later (what a reusable review should check).

**Status**: queued, not started

### Topic: Build a manually-run repo-review skill

Turn the periodic repo review (done manually this session) into a reusable, manually-invoked skill, usable both in this repo and in project repos (mounted via the standard share). It should audit the repo for gaps, inconsistencies, drift / stale cross-references, duplication, and sprawl, and surface suggestions for the human to weigh — report/propose only, never act without sign-off (cf. `init-project-docs`).

Keep it open-ended, not a fixed checklist: the agent should recommend what's worth reviewing based on what it actually finds, rather than mechanically walking a prescriptive list. A short set of standing prompts (sprawl caps, dangling references, duplication, docs-vs-reality drift) can seed it, but the agent should stay free to raise anything else it notices.

One concrete instance of the "introspection process for gradually improving the repo" item under Longer-term below.

**Status**: queued, not started

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger
