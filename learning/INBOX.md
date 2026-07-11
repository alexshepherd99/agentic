# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

- Mechanics of getting settled conventions into the repo
- Minimal setup to restructure an existing repo via Claude Code, then iterate
- Standard repo structure for persistent documents (requirements, plans, execution logs) — used consistently; sections may live within execution logs
- Where/how to record requirements and a backlog — manual for now, mechanics kept flexible
- Test-driven development — encourage where it makes sense

### Topic: Project onboarding guide for agentic

**Idea**: agentic should include a standard onboarding guide for
new project repos — the minimal steps a human follows once per repo, with
everything else embedded in agentic's own instructions rather than
duplicated per project.

**Minimal human steps (draft, not settled)**:
- Add `additionalDirectories` pointer to `../agentic` in
  `.claude/settings.json`
- Add a short pointer/section in the project's `CLAUDE.md` referencing the
  agentic conventions

**Open questions for deep dive**:
- What exactly goes in the guide vs. what's embedded in agentic's
  instructions themselves?
- How do project repos stay in sync if agentic's instructions change later?
  (stale `CLAUDE.md` pointer problem)
- Should this guide live in `conventions.md`, or as its own doc once it's
  no longer trivial?

**Status**: raw idea, not yet decided — related to the "Mechanics of
getting settled conventions into the repo" item above

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger
