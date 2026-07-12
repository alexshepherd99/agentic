# Collaboration workflow

The repo-agnostic working discipline for any piece of work, from first mention to done. Consumed by both `agentic`'s own `CLAUDE.md` and the `how-we-work` skill (project repos); each adds only its context-specific deltas and does not restate these points.

- **Ask before assuming.** When scope or requirements are ambiguous, ask several small, scoped questions rather than one open-ended one, and prefer asking over guessing. **Non-negotiable:** don't build on unstated assumptions. For larger or underspecified requests, use the `grill-me` skill to pressure-test the request and the plan first.
- **Propose before writing.** For any non-trivial or judgment-call change, present the approach — or the concrete diff/draft — and get confirmation before editing. Review-then-write, not write-then-revise. Trivial one-line fixes are exempt.
- **One change at a time, commit per item.** Work a multi-item task in an agreed order (flagging dependencies), committing each resolved item on its own with a descriptive message before starting the next. Don't batch unrelated changes into one commit.
- **Propose improvements to shared instructions.** When you spot a better practice mid-work, propose an update to the relevant convention, skill, or instructions file — propose, don't silently apply.
- **End-of-session review.** Near the end of a session with nontrivial back-and-forth, check that everything discussed landed somewhere durable, that no doc still frames a since-resolved decision as open, and that the working tree is clean and pushed.
