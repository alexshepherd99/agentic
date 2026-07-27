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

The working discipline for any change in a project repo, from first mention to done. Read this the moment a piece of work is raised — while requirements are still being discussed, before planning or code.

Start from the repo-agnostic core in `agentic`'s `shared/collaboration-workflow.md` — clarifying questions, propose-before-writing, commit-per-item, propose-improvements-to-shared-instructions, end-of-session review. This skill adds the project-repo specifics:

- **Definition of done: a green suite, reached from a red one.** In a repo with tests, confirm the relevant tests pass before starting a change, that each behavioural change was observed failing before it passed, and that the full suite is green before marking work complete. When presenting the work, say what failed and how — the diff can't show it afterwards.

(`agentic`'s own repo workflow is the sibling variant in its `CLAUDE.md`.)
