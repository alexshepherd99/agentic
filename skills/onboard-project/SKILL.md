---
name: onboard-project
description: Set up a project repo to consume this repo's (agentic's) shared agents/skills and conventions read-only. Trigger when the user asks to onboard a project, wire up agentic, set up access to shared skills/conventions, connect a project repo to the agentic repo, or reconcile a project's existing instruction files down to project-specific deltas.
---

# Onboard Project

Wires a project repo up to consume `agentic`'s `agents/`/`skills/`/conventions read-only, per the mechanics in `agentic`'s `learning/CONVENTIONS.md` ("Sharing agents/skills into project repos").

Run this from a session in the project repo, with `agentic` reachable (e.g. launched via `claude --add-dir ../agentic`, or already configured).

## Steps

1. **Confirm the relative path.** Find where `agentic` sits relative to the project repo (commonly `../agentic`, but confirm — don't assume). Use that path everywhere below.

2. **Write/update `.claude/settings.json`** in the project repo:
   ```json
   {
     "permissions": {
       "additionalDirectories": ["<relative-path-to-agentic>"],
       "deny": [
         "Write(<relative-path-to-agentic>/**)",
         "Edit(<relative-path-to-agentic>/**)"
       ]
     }
   }
   ```
   **Non-negotiable:** Merge into any existing config — never clobber unrelated settings.

3. **Add a short pointer section to the project's `CLAUDE.md`:**
   ```markdown
   ## Shared agents/skills/conventions

   This repo pulls in reusable agents, skills, and conventions from the
   `agentic` repo, mounted read-only at `<relative-path-to-agentic>`.
   See its `learning/CONVENTIONS.md` for settled decisions and
   `skills/`/`agents/` for what's available.

   Apply these shared skills as a matter of course:
   - **`how-we-work`** — the working discipline for any task; consult it at
     the very start of a piece of work, before planning or code.
   - **`coding-standards`** — how code here should be written; consult it
     before writing, modifying, or reviewing code.

   Propose changes to `agentic` by drafting text in this session — actual
   edits happen from a session whose working directory is `agentic` itself.
   ```
   Keep it a pointer, not a copy — don't duplicate `agentic`'s conventions content into the project. **Non-negotiable:** name the always-apply skills (`how-we-work`, `coding-standards`) explicitly — a plain mounted guidance file is easy to silently ignore, so the pointer is the backstop that surfaces them.

4. **Verify the deny rule actually holds.** Try to `Write`/`Edit` a dummy file inside the mounted `agentic` path (then clean it up), and confirm it's blocked. **Non-negotiable:** If it isn't blocked, tell the user explicitly and point them at the split-authority workflow in `agentic`'s `learning/CONVENTIONS.md` — the two-session discipline is the real safeguard; the deny rule is only a backstop.

5. **Reconcile the project's existing agent instructions.** Review any instruction files already in the repo (`CLAUDE.md`, `.github/copilot-instructions.md`, Cursor rules, etc.) against the principle that a project's instructions should hold *only* project-specific content — its differences from and overrides of `agentic`'s shared conventions/skills. Sort each existing rule into:
   - **Already covered by `agentic`** — redundant with the mounted shared content; propose deleting it.
   - **Generic but not yet in `agentic`** — repo-agnostic and worth sharing; propose migrating it out to `agentic` (convention or skill) and removing it here. The `agentic` edit is propose-only from a project session — it lands via the split-authority two-session workflow, not by writing to `agentic` from here.
   - **Project-specific difference/override** — keep it. This is the only category that should remain.
   - **Conflicts with `agentic`** — where the project's instructions contradict `agentic`'s `CONVENTIONS.md`/skills, flag it and ask which wins; don't silently reconcile.

   The end state is a project instruction file containing only project-specific deltas. **Non-negotiable:** propose the full sort and get sign-off before editing the project's files or drafting `agentic` changes — never trim or migrate automatically.

6. **Report back** what changed (settings.json diff, CLAUDE.md addition, verification result) rather than assuming silent success.

## Staleness

The pointer section is static prose, written once. If `agentic`'s structure changes significantly later, re-run this skill to refresh it — there's no automatic sync.

## Next step

Recommend running the `init-project-docs` skill to scaffold the project's own persistent-document structure (`BACKLOG.md`, `docs/<effort-name>/`) — a separate concern, kept separate so neither skill grows too large.
