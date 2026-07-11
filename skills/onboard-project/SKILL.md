---
name: onboard-project
description: Set up a project repo to consume this repo's (agentic's) shared agents/skills and conventions read-only. Trigger when the user asks to onboard a project, wire up agentic, set up access to shared skills/conventions, or connect a project repo to the agentic repo.
---

# Onboard Project

Wires a project repo up to consume `agentic`'s `agents/`/`skills/`/conventions read-only, per the mechanics in `agentic`'s `learning/CONVENTIONS.md` ("Sharing agents/skills into project repos").

Run this from a session in the project repo, with `agentic` reachable (e.g. launched via `claude --add-dir ../agentic`, or already configured).

## Steps

1. **Confirm the relative path.** Find where `agentic` actually sits relative to the project repo (commonly `../agentic`, but confirm — don't assume). Use that path everywhere below.

2. **Write/update `.claude/settings.json`** in the project repo, merging into any existing config (don't clobber unrelated settings):
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

3. **Add a pointer section to the project's `CLAUDE.md`**, something like:
   ```markdown
   ## Shared agents/skills/conventions

   This repo pulls in reusable agents, skills, and conventions from the
   `agentic` repo, mounted read-only at `<relative-path-to-agentic>`.
   See its `learning/CONVENTIONS.md` for settled decisions and
   `skills/`/`agents/` for what's available. Propose changes there by
   drafting text in this session — actual edits happen from a session
   whose working directory is `agentic` itself.
   ```
   Keep this section short — it's a pointer, not a copy. Don't duplicate `agentic`'s conventions content into the project's `CLAUDE.md`.

4. **Verify the deny rule actually holds.** Try to `Write` or `Edit` a dummy file inside the mounted `agentic` path (e.g. a scratch file, then clean it up). Confirm the operation is blocked. If it isn't, tell the user explicitly and point them at the split-authority workflow in `agentic`'s `learning/CONVENTIONS.md` as the real safeguard (two-session discipline: only commit to `agentic` from a session whose working directory is `agentic` itself).

5. **Report back** what was changed (settings.json diff, CLAUDE.md addition, verification result) rather than assuming silent success.

## Note on staleness

This pointer section is static prose, written once. If `agentic`'s structure changes significantly later, re-run this skill on the project to refresh it — there's no automatic sync.
