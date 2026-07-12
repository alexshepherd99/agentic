# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

There is no code, build, lint, or test tooling. This repo has two roles:

1. A personal scratchpad for learning agentic engineering (Claude Code, agentic workflows, repo structure, skills) — content lives under `learning/`.
2. The home for reusable agents and skills, pulled into other project repos so they don't have to be duplicated per-project.

## Workflow

Commit directly to `main` — no feature branches or PRs for changes to this repo.

## Agents and skills (`agents/`, `skills/`)

Canonical content lives in tool-agnostic form so it isn't tied to Claude Code specifically:

```
agents/<agent-name>/agent.md   # frontmatter: name, description — body: instructions
skills/<skill-name>/SKILL.md   # frontmatter: name, description — body: instructions
                                 # (optional supporting files can live alongside SKILL.md)
```

Frontmatter is deliberately limited to `name` and `description` — no tool-specific fields (Claude Code's `tools`, `model`, etc.) belong in the canonical files, so this content can be read or adapted by other coding agents (Copilot, Cursor, etc.), not just Claude Code.

`.claude/agents` and `.claude/skills` are symlinks to the top-level `agents/` and `skills/` folders. They exist purely so Claude Code can discover this content today via `/add-dir <path-to-this-repo>` — the top-level folders remain the single source of truth; don't edit through the symlinks or duplicate content into them.

## Shared instruction (`shared/`)

Runtime instruction needed in more than one place — across skills, or by this file's own conventions — extracted here so it isn't duplicated (e.g. `shared/persistent-docs.md`, the project persistent-document structure; `shared/collaboration-workflow.md`, the collaboration discipline). Created only when the need actually arises; one file per concern. Distinct from `learning/CONVENTIONS.md`, which records settled decisions and rationale and is *not* loaded at skill runtime.

## Knowledge base structure (`learning/`)

- `INBOX.md` — raw, messy capture of ideas, links, and half-formed thoughts. A completed item can be deleted from the list once it's fully done **and** its outputs are persisted somewhere durable (a commit, a `CONVENTIONS.md` entry, a skill, or a memory) — the INBOX tracks open work, not history.
- `CONVENTIONS.md` — settled decisions (repo structure, naming, workflow patterns) — this is what eventually gets copied into a real repo

Treat `learning/` as a staging area, not a source of truth — finished material eventually gets promoted out into actual git repos.

## Working conventions

The repo-agnostic collaboration discipline lives in `shared/collaboration-workflow.md` — read it (clarifying questions, propose-before-writing, commit-per-item, propose-improvements-to-shared-instructions, end-of-session review). This repo adds:

- **Ask before adding to the knowledge base.** When something in a chat looks like it should persist (a decision, a convention, a completed idea), ask before adding it — don't add automatically, and don't assume something is settled just because it was discussed at length.
- **Watch for sprawl.** Periodically (roughly every 10–15 chats, or whenever proposing an addition), check the knowledge base and flag it for review/consolidation if:
  - There are more than ~8–10 documents
  - Any single document exceeds ~1,500 words
  - Documents seem to overlap in coverage
  - Answering a simple question requires searching across multiple docs
- **End-of-session review — also** confirm the knowledge base is captured and consistent: everything discussed lives in the INBOX/CONVENTIONS/a memory/a commit, no doc frames a since-resolved decision as open, and sprawl (above) is in check.
