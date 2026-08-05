# Persistent documents in project repos

Standard structure for a project repo's requirements, plans, and execution logs, so agents and humans always know where to look.

- **`BACKLOG.md`** (repo root) — global list of not-yet-started work. Freeform; one file, one list.
- **`docs/<effort-name>/`** — created when an item is picked up off the backlog and work starts. Holds that effort's `requirements.md`, `plan.md`, and `log.md`.
- **Collapsing for small efforts** — a trivial effort can skip the separate files and use a single `log.md` with inline `## Requirements` / `## Plan` sections instead. Split them out once any one section gets unwieldy.
- **Logs are curated prose, not a transcript.** Record the decision, the outcome, and the reasoning — not raw command output.
  - Quote output only where the exact text is the point (an error message, a surprising value), and then only the lines that carry it.
  - Reporting *in session* is different: quoting a real failure there is expected. This governs what lands in the file.
- **Superseded content is annotated in place, not rewritten or deleted** — a requirement or plan step that stops being true keeps its original wording and gains a dated marker beside it. The effort's history stays readable, and a reader can see what was believed when.
  - Inline `[Superseded YYYY-MM-DD: …]` for a sentence; a blockquote for a whole step.
  - This includes lists of files an effort touched: a file deleted during the effort stays listed, marked with its deletion date and a recovery SHA, rather than dropped.
  - `log.md` is append-only by nature — correct it with a new entry, never by editing an old one.
