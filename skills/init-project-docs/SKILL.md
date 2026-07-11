---
name: init-project-docs
description: Scaffold or review a project repo's persistent-document structure (BACKLOG.md, docs/<effort-name>/{requirements,plan,log}.md). Trigger when starting a new effort/feature that needs tracked requirements/plan/log, when a repo has no BACKLOG.md yet, or when asked to review/migrate existing docs into this structure.
---

# Init Project Docs

Sets up this repo's standard persistent-document structure (see the `agentic` repo's `learning/CONVENTIONS.md`, "Persistent documents in project repos"):

- `BACKLOG.md` at the repo root — a global, freeform list of not-yet-started work.
- `docs/<effort-name>/` per effort in progress, holding `requirements.md`, `plan.md`, `log.md`.

## Two things this skill does

1. **Scaffold.** If `BACKLOG.md` doesn't exist, create an empty one. When starting a new effort, create `docs/<effort-name>/` with the three files (or just `log.md` if the effort is small enough — see the collapsing rule in CONVENTIONS.md).

2. **Review and propose migration.** Look for existing requirements/plan/log-like documents already in the repo (a README with a "Plan" section, a TODO.md, design docs, etc.). Report what was found and how it would map onto the new structure. **Never move or rewrite files automatically** — propose the mapping, let the human decide, then act only if approved.

## Note

This is deliberately a separate skill from `onboard-project` — that one wires up the mount to the `agentic` repo itself; this one is about a project's own document structure once work starts. Keeping them separate avoids either skill growing too large to reliably follow.
