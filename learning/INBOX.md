# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

### Topic: Project instructions should only hold project specifics

**Principle**: a project repo's own agent instructions (`CLAUDE.md`, `.github/copilot-instructions.md`, etc.) should contain only project-specific content. Anything generic/repo-agnostic belongs in this `agentic` repo instead (as a convention or skill), not duplicated per-project.

**Action needed**: as part of repo setup, any existing Copilot/agent instructions in a project repo should be reviewed against this principle:
- Flag generic content that should be migrated out to `agentic` (convention/skill), rather than left duplicated in the project's own instructions.
- Flag inconsistencies between what the project's instructions say and what's already settled in `agentic`'s `CONVENTIONS.md`/skills.

Likely lands as a review step added to the `onboard-project` skill. The import/packaging work this depended on is now done (the `how-we-work` and `coding-standards` skills exist, and CONVENTIONS points at them), so there's real content to test the review against.

**Status**: queued, not started

### Topic: Final duplication sweep — learning files vs baked skills

One last pass checking for leftover duplication between the `learning/` files (`CONVENTIONS.md`, `INBOX.md`, `README.md`) and the baked skills/READMEs (`how-we-work`, `coding-standards`, `onboard-project`, `init-project-docs`, `grill-me`, plus `shared/persistent-docs.md`). Where a skill now owns a rule, `CONVENTIONS.md` should reference it once, not restate it — remove any restatement that remains.

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
