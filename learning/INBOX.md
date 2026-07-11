# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

### Topic: Import Copilot instructions, then package everything for project use

Two-part plan for a fresh session:

1. **Bring in Copilot instructions from a previous project.** Review them and convert whatever is generic/repo-agnostic (not tied to that specific project) into settled conventions in this repo's `CONVENTIONS.md`.
2. **Package everything for project consumption.** Once that's done, sweep everything in this repo that's meant for other projects to use but isn't already a skill (e.g. convention entries that are really guidance for how a project should behave, not just decisions about this repo) — turn each into whatever form actually fits: a skill, an agent, or a plain guidance file that project repos read. Form is flexible; the point is making it consumable, not just documented here.

**Status**: queued, not started

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger
