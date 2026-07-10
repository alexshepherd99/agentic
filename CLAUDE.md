# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

There is no code, build, lint, or test tooling. This repo has two roles:

1. A personal scratchpad for learning agentic engineering (Claude Code, agentic workflows, repo structure, skills) — content lives under `learning/`.
2. The intended home for Claude Code agents and skills meant to be reused across other project repos, pulled in there via Claude Code's "Additional repos" feature. This part is still being built out.

## Workflow

Commit directly to `main` — no feature branches or PRs for changes to this repo.

## Knowledge base structure (`learning/`)

- `INBOX.md` — raw, messy capture of ideas, links, and half-formed thoughts
- `CONVENTIONS.md` — settled decisions (repo structure, naming, workflow patterns) — this is what eventually gets copied into a real repo
- `SKILLS-AND-TECHNIQUES.md` — specific techniques, skills, or patterns being evaluated but not yet adopted

Treat `learning/` as a staging area, not a source of truth — finished material eventually gets promoted out into actual git repos.

## Working conventions

- **Ask before adding to the knowledge base.** When something in a chat looks like it should persist (a decision, a convention, a completed idea), ask before adding it — don't add automatically, and don't assume something is settled just because it was discussed at length.
- **Watch for sprawl.** Periodically (roughly every 10–15 chats, or whenever proposing an addition), check the knowledge base and flag it for review/consolidation if:
  - There are more than ~8–10 documents
  - Any single document exceeds ~1,500 words
  - Documents seem to overlap in coverage
  - Answering a simple question requires searching across multiple docs
