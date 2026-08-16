---
name: review-repo-health
description: Review a whole repository as it stands — docs, instruction content, structure and code — for gaps, stale cross-references, duplication, sprawl, and drift between what the docs claim and what the repo contains. Trigger only when the user explicitly asks for a repo review, health check or audit; never on a cadence, never inside other work.
---

# Review repository health

Scope is the repository as it now stands — README and instruction files, structure, docs, code. A diff-scoped review sees only what changed; this looks at what accumulated.

**Non-negotiable: run this on request, in a session of its own.** Never start one because the current session noticed something, and never put it on a cadence. Capture the observation, offer to close, come back to it. The repo-wide-audit clause in `agentic`'s `shared/collaboration-workflow.md` is why.

**Non-negotiable: report and propose; change nothing without sign-off.** Findings are for the human to weigh. Fixing one while reviewing turns a review into implementation work, which is the thing the rule above exists to prevent.

## Judgment, not a checklist

The seeds below are a starting point, not the scope. Read what the repo actually contains and raise whatever you find — a finding outside every seed is the reason to run this rather than a script. A seed that turns up nothing gets one line, not a paragraph defending the absence.

Rank findings by what a reader or an agent loses to each one — being sent to content that isn't there, or acting on a doc the code stopped matching, costs more than an untidy heading. Order by that cost, not by how easy each is to fix.

## Seeds

Each is a class the 2026-07 full-repo pass actually found.

- **Stale cross-references.** A doc pointing elsewhere for content that isn't there, or naming a file, folder or section that has moved or gone.
- **Docs-vs-reality drift.** A structure or overview doc missing a folder that exists; a documented command that no longer runs; a convention the code stopped following. Confirm by running or looking, not by reading the doc.
- **Duplication.** The same rule stated in an always-loaded doc and again in a skill. Repeated *citation* phrasing is the consistency convention working — `agentic`'s `shared/instruction-hygiene.md` draws that line.
- **Front doors that never say what the thing is.** A README or entry doc that explains usage without stating what it is or who it's for.
- **Sprawl.** Document count, document size, and whether answering a simple question takes several docs.
- **Unclear sibling relationships.** Adjacent sections or files whose division of labour a reader can't infer.
- **Code.** Judge against `coding-standards`, and look for what a diff review structurally can't see — dead code, an entry point no test exercises, a module the structure has outgrown.

## Seeding the next review

A review that finds a class of problem no seed anticipated should propose adding it as a seed here. Judge it the same way as any other finding — what a future reader or agent gains from having it — not by whether it was a surprise. One instance that cost a reader something earns a seed; one that merely hadn't been listed does not.

Editing this file from a project repo needs `agentic`'s `propose-shared-change`, since the mount is read-only.

## Seeding from the hygiene tool

In `agentic`, start with `python3 tools/instruction_hygiene.py --all` and triage per `shared/instruction-hygiene.md`. Its flags are input to the judgment pass, never findings on their own. The tool resolves paths from `agentic`'s root, so it cannot be pointed at a project repo's own files — there, apply the thresholds by reading.

## Landing the findings

Report in the session first, then offer to persist what the user accepts — `learning/INBOX.md` in `agentic`, `BACKLOG.md` in a project repo. Record what was considered and rejected too, with the reason, so the next review doesn't re-raise it.

## Out of scope

- Credentials, identifying data and weakened controls — `review-repo-security`. Also a session of its own; don't fold either into the other.
- An incoming proposal checked against its target file — `propose-shared-change`.
