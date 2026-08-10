---
name: reconcile-project-instructions
description: Reduce a project repo's own agent instructions (CLAUDE.md, .github/copilot-instructions.md, Cursor rules) to only its project-specific deltas from agentic's shared conventions and skills. Trigger when an onboarded project's instruction files still restate, contradict, or predate the shared content, or when asked to review, trim, or migrate a project's existing instructions.
---

# Reconcile Project Instructions

Reviews the instruction files already in a project repo against the principle that a project's instructions should hold *only* project-specific content — its differences from and overrides of `agentic`'s shared conventions and skills. `learning/CONVENTIONS.md` records that decision; this skill is the procedure.

Run from a session in the project repo, with `agentic` reachable. The `onboard-project` skill wires up that mount and is the source of truth for those mechanics; this skill assumes it has already run.

## Steps

1. **Sort every existing rule.** Review any instruction files already in the repo (`CLAUDE.md`, `.github/copilot-instructions.md`, Cursor rules, etc.) and sort each rule into:
   - **Already covered by `agentic`** — redundant with the mounted shared content; propose deleting it.
   - **Generic but not yet in `agentic`** — repo-agnostic and worth sharing; propose migrating it out to `agentic` (convention or skill) and removing it here. The `agentic` edit is propose-only from a project session — it lands via the `propose-shared-change` skill's handoff, not by writing to `agentic` from here.
   - **Project-specific difference/override** — keep it. This is the only category that should remain.
   - **Conflicts with `agentic`** — where the project's instructions contradict `agentic`'s `CONVENTIONS.md`/skills, flag it and ask which wins; don't silently reconcile.

2. **Get sign-off, then apply.** The end state is a project instruction file containing only project-specific deltas. **Non-negotiable:** propose the full sort and get sign-off before editing the project's files or drafting `agentic` changes — never trim or migrate automatically.

3. **Report back** what changed and what was migrated out, rather than assuming silent success.
