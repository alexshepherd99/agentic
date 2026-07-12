---
name: how-we-work
description: How to work through ANY piece of work in a project repo — ask scoped
  clarifying questions before assuming, propose the approach/diff before editing,
  one change per commit with a descriptive message, start from and end on a green
  test suite, end-of-session review. Read at the VERY START of a task — the moment
  a requirement, feature, bug, or change is first raised, discussed, or proposed,
  before any planning or code — NOT deferred until code is touched.
---

# How we work (project repos)

The working discipline for any change in a project repo, from first mention to done. Read this the moment a piece of work is raised — while requirements are still being discussed, before planning or code. (This is the coding-project workflow; `agentic`'s own repo workflow lives in its `CLAUDE.md`.)

- **Ask before assuming.** When scope or requirements are ambiguous, ask several small, scoped questions rather than one open-ended one, and prefer questions over guessing. **Non-negotiable:** don't build on unstated assumptions. For larger or underspecified tasks, use the `grill-me` skill to pressure-test the request and the plan first.
- **Propose the approach before writing.** For any non-trivial change, present the plan — or the concrete diff for a judgment call — and get confirmation before editing. Review-then-write, not write-then-revise. Trivial one-line fixes are exempt.
- **One change at a time, commit per item.** Work a multi-item task in an agreed order (flagging dependencies), committing each resolved item on its own — with a descriptive message — before starting the next. Don't batch unrelated changes into one commit.
- **Definition of done: a green suite.** In a repo with tests, confirm the relevant tests pass before starting a change, and that the full suite is green before marking work complete.
- **Propose improvements to shared instructions.** When you spot a better practice mid-work, propose an update to the relevant convention, skill, or instructions file — propose, don't silently apply.
- **End-of-session review.** Near the end of a working session, check that everything discussed landed somewhere durable (a commit, a tracked doc/issue), that no doc still frames a resolved decision as open, and that the working tree is clean and pushed.
