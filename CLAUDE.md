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
- **Draft before writing.** For judgment-call or multi-paragraph content (a convention, a skill/agent file), show the full draft in chat and get explicit confirmation before Edit/Write — review-then-write, not write-then-revise. Trivial one-line fixes are exempt.
- **Ask clarifying questions.** When anything is ambiguous, prefer several small, scoped questions over one big open-ended one — don't finalize on assumptions.
- **One item at a time, commit per item.** Work multi-item lists in an order you pick (flagging dependencies), committing and pushing each resolved item before the next — don't batch several into one commit.
- **End-of-session review.** Near the end of a session with nontrivial back-and-forth, proactively check that everything discussed was captured somewhere durable (commit, INBOX/CONVENTIONS entry, memory), that no file still frames a since-resolved decision as open, that the tree is clean/pushed, and that sprawl (see above) is in check.
