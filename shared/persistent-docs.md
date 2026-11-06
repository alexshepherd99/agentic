# Persistent documents in project repos

Standard structure for a project repo's requirements, plans, and execution logs, so agents and humans always know where to look.

- **`BACKLOG.md`** (repo root) — global list of not-yet-started work. Freeform; one file, one list.
- **`docs/<effort-name>/`** — created when an item is picked up off the backlog and work starts. Holds that effort's `requirements.md`, `plan.md`, and `log.md`.
- **Collapsing for small efforts** — a trivial effort can skip the separate files and use a single `log.md` with inline `## Requirements` / `## Plan` sections instead. Split them out once any one section gets unwieldy.
- **Gates, where verification needs an environment you cannot reach on demand** — hardware, a device, a staging tier, anything intermittent or costly. Rather than blocking milestones on access or deferring everything to the end, collect the environment-dependent checks into numbered gates in `plan.md`, each a short checklist.
  - Milestones reach **done (dev)** without the environment; a gate reaches **done (verified)**. Keep the two labels distinct, so nothing is claimed as working somewhere it has never run.
  - Work continues past an uncleared gate. A gate blocks only the claim that its milestone is verified, never the next milestone.
  - Gates are cleared in batches when access happens, which is also why milestone order is worth arranging around them.
  - Expect a gate to find several defects at once. That is the mechanism working: they would otherwise have been found one visit at a time.
- **Logs are curated prose, not a transcript.** Record the decision, the outcome, and the reasoning — not raw command output.
  - Quote output only where the exact text is the point (an error message, a surprising value), and then only the lines that carry it.
  - Reporting *in session* is different: quoting a real failure there is expected. This governs what lands in the file.
  - `log.md` is append-only — correct it with a new entry, never by editing an old one.
  - **A long effort rolls its log.** When a milestone or gate closes, move its entries and everything older into `log-archive.md`, leaving the current milestone's in `log.md`. Nothing is rewritten and nothing is deleted: the text is identical, in a file beside it, so a pointer that names an entry by its heading still resolves.
    - The trigger is mechanical on purpose. Entries move because their milestone is finished, never because someone judged they would not be wanted again — that judgement is a prediction, and a wrong one buries the reasoning you turn out to need.
    - The archive is not read on orientation. A session reads `requirements.md`, `plan.md` and the current `log.md`, and opens the archive only when investigating something specific. That is what the roll is for.
    - Roll only once the log has grown past the point where it is read end to end. A short effort never needs to.
- **Apply the identifying-data rule while writing, not at review.** Effort docs describe real runs on real machines, which makes them the likeliest route for an address, hostname, path, ISP or location to enter a repo — and the least likely text to be re-read later. Logs are the sharpest case, being written fastest and quoted from real output.
  - Before recording a measurement, ask what it reveals about the machine or its owner, and write the finding without it. "A real run produced plausible figures" carries the same evidence as the figures.
  - Machine-specific paths are the easy one to miss, because they arrive by accident: an absolute path pasted into a doc, a test fixture, or an error message carries a username and a directory layout.
  - Real measurements belong in whatever the project stores data in, which is not tracked. The doc records what was learned from them.
  - **Quoting a value in order to explain why it is sensitive still commits the value.** The sentence is *about* protecting the data, which makes it read as legitimate while being written, and a scanner cannot tell the two uses apart. Name the category — "a private address", "the ISP" — never the value.
  - Catching this at review means it was already committed, and possibly already pushed. There is no equivalent of rotation for it.
- **Plans and requirements are living documents; the log is the history.** `plan.md` and `requirements.md` show what is true now and are edited in place when that changes, with no superseded markers. Git holds the old wording, and the log holds the reasoning.
  - **A change beyond progress gets a log entry in the same commit**, saying what changed and why. Marking a step done is progress; adding, reordering, replacing or dropping one is not. This is what stops a living plan drifting silently.
  - **A settled decision lands in `plan.md` or `requirements.md`, not only in the log.** Anything a later session must not have to re-litigate goes into one of them when it is settled — the log narrates a decision, it does not store it.
  - **A finished step collapses to one line** pointing to its log entry, so references to it still resolve and a reader sees what is built without reading how. A step replaced rather than finished gets a one-line "replaced by N". Step numbers are never reused.
  - **A rejected or reversed option stays in `requirements.md` as one line** — what, when, why, and a log pointer — so a later session sees what not to propose again without reading the history.
  - A file deleted during the effort leaves the plan's file lists; its deletion date and a recovery SHA go in the log.
  - Converting an effort written under the old annotate-in-place rule starts by checking that every marker in it has a matching log entry, writing any that are missing, before the file is rebuilt. Finished efforts are left as they are.
