# Persistent documents in project repos

Standard structure for a project repo's requirements, plans, and execution logs, so agents and humans always know where to look.

- **`BACKLOG.md`** (repo root) — global list of not-yet-started work. Freeform; one file, one list.
- **`docs/<effort-name>/`** — created when an item is picked up off the backlog and work starts. Holds that effort's `requirements.md`, `plan.md`, and `log.md`.
- **Collapsing for small efforts** — a trivial effort can skip the separate files and use a single `log.md` with inline `## Requirements` / `## Plan` sections instead. Split them out once any one section gets unwieldy.
