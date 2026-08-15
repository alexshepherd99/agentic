# Persistent documents in project repos

Standard structure for a project repo's requirements, plans, and execution logs, so agents and humans always know where to look.

- **`BACKLOG.md`** (repo root) — global list of not-yet-started work. Freeform; one file, one list.
- **`docs/<effort-name>/`** — created when an item is picked up off the backlog and work starts. Holds that effort's `requirements.md`, `plan.md`, and `log.md`.
- **Collapsing for small efforts** — a trivial effort can skip the separate files and use a single `log.md` with inline `## Requirements` / `## Plan` sections instead. Split them out once any one section gets unwieldy.
- **Logs are curated prose, not a transcript.** Record the decision, the outcome, and the reasoning — not raw command output.
  - Quote output only where the exact text is the point (an error message, a surprising value), and then only the lines that carry it.
  - Reporting *in session* is different: quoting a real failure there is expected. This governs what lands in the file.
- **Apply the identifying-data rule while writing, not at review.** Effort docs describe real runs on real machines, which makes them the likeliest route for an address, hostname, path, ISP or location to enter a repo — and the least likely text to be re-read later. Logs are the sharpest case, being written fastest and quoted from real output.
  - Before recording a measurement, ask what it reveals about the machine or its owner, and write the finding without it. "A real run produced plausible figures" carries the same evidence as the figures.
  - Machine-specific paths are the easy one to miss, because they arrive by accident: an absolute path pasted into a doc, a test fixture, or an error message carries a username and a directory layout.
  - Real measurements belong in whatever the project stores data in, which is not tracked. The doc records what was learned from them.
  - **Quoting a value in order to explain why it is sensitive still commits the value.** The sentence is *about* protecting the data, which makes it read as legitimate while being written, and a scanner cannot tell the two uses apart. Name the category — "a private address", "the ISP" — never the value.
  - Catching this at review means it was already committed, and possibly already pushed. There is no equivalent of rotation for it.
- **Superseded content is annotated in place, not rewritten or deleted** — a requirement or plan step that stops being true keeps its original wording and gains a dated marker beside it. The effort's history stays readable, and a reader can see what was believed when.
  - Inline `[Superseded YYYY-MM-DD: …]` for a sentence; a blockquote for a whole step.
  - This includes lists of files an effort touched: a file deleted during the effort stays listed, marked with its deletion date and a recovery SHA, rather than dropped.
  - `log.md` is append-only by nature — correct it with a new entry, never by editing an old one.
