---
name: how-we-work
description: How to work through ANY piece of work in a project repo — ask scoped
  clarifying questions before assuming, propose the approach/diff before editing,
  one change per commit with a descriptive message, start from and end on a green
  test suite, end-of-session review. Read at the VERY START of a task — the moment
  a requirement, feature, bug, or change is first raised, discussed, or proposed,
  before any planning or code — NOT deferred until code is touched.
---

<!-- hygiene-ok: description_max_words — the trigger terms carry the "read at the very start" timing, which is the rule this skill exists to enforce; cutting them makes it fire later. 2026-07-30 -->

# How we work (project repos)

The working discipline for any change in a project repo, from first mention to done. Read this the moment a piece of work is raised — while requirements are still being discussed, before planning or code.

Start from the repo-agnostic core in `agentic`'s `shared/collaboration-workflow.md`. This skill adds the project-repo specifics:

- **Definition of done: a green suite, reached from a red one.** In a repo with tests, confirm:
  - the relevant tests pass before starting a change;
  - each behavioural change was observed failing before it passed;
  - the full suite is green before marking work complete.

  When presenting the work, say what failed and how — the diff can't show it afterwards.

- **Definition of done, second clause: it has been run.** A green suite is evidence the logic is right, not that the thing works.
  - Code that touches a real system — installers, service units, deploy scripts, anything shelling out or writing outside the process — is not done until it has been executed against that system.
  - **Non-negotiable:** when reporting work complete, name what has *not* been executed. "Tests pass" and "it runs" are different claims and must not be merged into one.
  - Where the real system is expensive or intermittent to reach, batch the checks rather than skipping them — see the gates convention in `shared/persistent-docs.md`.

(`agentic`'s own repo workflow is the sibling variant in its `CLAUDE.md`.)
