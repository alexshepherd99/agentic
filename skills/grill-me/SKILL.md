---
name: grill-me
description: Interrogate an ambiguous or underspecified request before acting on it, then pressure-test the resulting plan before implementing. Trigger automatically when a request has unstated assumptions, missing scope/requirements, or multiple reasonable interpretations. Skip for requests that are already fully specified, small edits, or straightforward bug fixes — grilling those just adds friction. Also trigger whenever the user explicitly says "grill me," asks to stress-test a plan, or asks what they're missing.
---

# Grill Me

Interrogate a request or plan before acting on it, rather than proceeding on assumptions.

## Workflow: Grill first, Decide second, Implement third, Review fourth

Two grilling stages, not one:

1. **Grill the request.** Before forming a plan, surface the request's fuzzy parts — unstated assumptions, ambiguous scope, edge cases, "why X and not Y." Ask one question at a time, like walking a decision tree branch by branch, rather than dumping a long list. Stop once the request has an explicit, shared, unambiguous meaning.
2. **Grill the plan.** Once an approach exists — before implementing — pressure-test the plan itself with forcing questions:
   - "Why X and not Y?"
   - "What's the kill criterion?"
   - "What's blocking this — and when does the blocker resolve?"
   - "Which side of the trade-off, and what's the constraint?"
   - "Even at 60% confidence — what's your best guess?"

Don't skip straight to implementation just because a plan sounds plausible — an underspecified request stays underspecified until it's actually been grilled.

## Record of the exchange

Once a request has been grilled, write the resolved understanding to `docs/<effort-name>/requirements.md` (use the `init-project-docs` skill to create the effort folder if it doesn't exist yet). Once a plan has been grilled, write the resolved plan to `docs/<effort-name>/plan.md`. Record the settled answers and decisions, not a transcript of the back-and-forth. For a trivial effort, collapse into `docs/<effort-name>/log.md` with `## Requirements` / `## Plan` sections instead — see the collapsing rule in `agentic`'s `learning/CONVENTIONS.md`.

## Source

Adapted from the established "grill-me" pattern in the Claude Code skill ecosystem — see https://claudemarketplaces.com/skills/mattpocock/skills/grill-me
