# Agentic engineering topics to explore

## Ideas

- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger
- "Grill me"-style skill — active challenge before starting work, with a record of the exchange
- Standard repo structure for persistent documents (requirements, plans, execution logs) — used consistently; sections may live within execution logs
- Where/how to record requirements and a backlog — manual for now, mechanics kept flexible
- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Minimal setup to restructure an existing repo via Claude Code, then iterate
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Test-driven development — encourage where it makes sense
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Mechanics of getting settled conventions into the repo

## Topic: Project onboarding guide for agentic-scratchpad

**Idea**: agentic-scratchpad should include a standard onboarding guide for
new project repos — the minimal steps a human follows once per repo, with
everything else embedded in the scratchpad's own instructions rather than
duplicated per project.

**Minimal human steps (draft, not settled)**:
- Add `additionalDirectories` pointer to `../agentic-scratchpad` in
  `.claude/settings.json`
- Add a short pointer/section in the project's `CLAUDE.md` referencing the
  scratchpad conventions

**Open questions for deep dive**:
- What exactly goes in the guide vs. what's embedded in scratchpad
  instructions themselves?
- How do project repos stay in sync if scratchpad instructions change later?
  (stale `CLAUDE.md` pointer problem)
- Should this guide live in `conventions.md`, or as its own doc once it's
  no longer trivial?

**Status**: raw idea, not yet decided — related to inbox item #15
("Mechanics of getting settled conventions into the repo")
