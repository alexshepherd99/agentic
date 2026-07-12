---
name: init-project-docs
description: Scaffold or review a project repo's persistent-document structure (BACKLOG.md, docs/<effort-name>/{requirements,plan,log}.md). Trigger when starting a new effort/feature that needs tracked requirements/plan/log, when a repo has no BACKLOG.md yet, or when asked to review/migrate existing docs into this structure.
---

# Init Project Docs

Sets up a project repo's standard persistent-document structure — see `agentic`'s `shared/persistent-docs.md` for the structure and collapsing rule:

- `BACKLOG.md` at the repo root — a global, freeform list of not-yet-started work.
- `docs/<effort-name>/` per effort in progress, holding `requirements.md`, `plan.md`, `log.md`.

## Two things this skill does

1. **Scaffold.** If `BACKLOG.md` doesn't exist, create an empty one. When starting a new effort, create `docs/<effort-name>/` with the three files (or just `log.md` if the effort is small — see the collapsing rule in `agentic`'s `shared/persistent-docs.md`).
2. **Review and propose migration.** Look for existing requirements/plan/log documents already in the repo (a README with a "Plan" section, a TODO.md, design docs). Report what was found and how it would map onto the structure.

**Non-negotiable:** Never move or rewrite files automatically. Propose the mapping, let the human decide, then act only if approved.

## Note

Separate from `onboard-project` (which wires up the mount to the `agentic` repo) on purpose — this skill covers a project's own document structure once work starts. Keeping them separate stops either from growing too large to follow reliably.
