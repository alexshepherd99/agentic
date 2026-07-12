---
name: grill-me
description: Interrogate an ambiguous or underspecified request before acting on it, then pressure-test the resulting plan before implementing. Trigger automatically when a request has unstated assumptions, missing scope/requirements, or multiple reasonable interpretations. Skip for requests that are already fully specified, small edits, or straightforward bug fixes — grilling those just adds friction. Also trigger whenever the user explicitly says "grill me," asks to stress-test a plan, or asks what they're missing.
---

# Grill Me

Interrogate a request or plan before acting on it, rather than proceeding on assumptions.

## Two grilling stages

1. **Grill the request** — before forming a plan. Surface the fuzzy parts: unstated assumptions, ambiguous scope, edge cases, "why X and not Y." Stop once the request has an explicit, shared, unambiguous meaning.
2. **Grill the plan** — once an approach exists, before implementing. Pressure-test it with forcing questions:
   - "Why X and not Y?"
   - "What's the kill criterion?"
   - "What's blocking this — and when does the blocker resolve?"
   - "Which side of the trade-off, and what's the constraint?"
   - "Even at 60% confidence — what's your best guess?"

**Non-negotiable:** Ask one question at a time, walking the decision tree branch by branch — never dump a long list.

**Non-negotiable:** Don't skip to implementation because a plan sounds plausible. An underspecified request stays underspecified until it has actually been grilled.

## Record the exchange

Once the request is grilled, write the resolved understanding to `docs/<effort-name>/requirements.md`; once the plan is grilled, write the resolved plan to `docs/<effort-name>/plan.md`. Record the settled decisions, not a transcript of the back-and-forth. For a trivial effort, collapse into `log.md` instead. See `agentic`'s `shared/persistent-docs.md` for the structure and collapsing rule, and the `init-project-docs` skill to create the folder if it doesn't exist yet.
