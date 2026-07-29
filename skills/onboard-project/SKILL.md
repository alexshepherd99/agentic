---
name: onboard-project
description: Set up a project repo to consume this repo's (agentic's) shared agents/skills and conventions read-only. Trigger when the user asks to onboard a project, wire up agentic, set up access to shared skills/conventions, connect a project repo to the agentic repo, or reconcile a project's existing instruction files down to project-specific deltas.
---

# Onboard Project

Wires a project repo up to consume `agentic`'s `agents/`/`skills/`/conventions read-only. This skill is the source of truth for the mechanics.

Run this from a session in the project repo, with `agentic` reachable (e.g. launched via `claude --add-dir ../agentic`, or already configured).

## Steps

1. **Capture the path in both forms it's needed in.** Find where `agentic` sits relative to the project repo (commonly `../agentic`, but confirm — don't assume). Two consumers, two forms, not interchangeable:
   - **Relative** (e.g. `../agentic`) — for `additionalDirectories` (step 2) and the `CLAUDE.md` pointer prose (step 3), where it reads as "where the mount is".
   - **Home-rooted glob** — literally `~/**/agentic/**`, for the deny rule (step 2). Deny rules only anchor against `~/`-rooted paths; a relative or unanchored path silently matches nothing. Keep the `**` wildcard rather than substituting the real checkout path — it stays committable (no username, no assumed layout) and still resolves to "an `agentic` repo somewhere under `$HOME`". If `agentic` lives outside `$HOME`, this won't match — root the glob at wherever it does live, and lean on step 4 to confirm.

2. **Write/update `.claude/settings.json`** in the project repo:
   ```json
   {
     "permissions": {
       "additionalDirectories": ["<relative-path-to-agentic>"],
       "deny": [
         "Edit(~/**/agentic/**)"
       ]
     }
   }
   ```
   No `Write(...)` companion rule: file-permission checks consult only `Edit(path)` rules, and an `Edit` rule already covers every file-editing tool (Write, Edit, NotebookEdit). A `Write(...)` deny rule is dead config, and Claude Code prints a startup warning saying so.

   `additionalDirectories` is a separate mechanism from deny matching, and the relative form there hasn't been probe-tested the way the deny rule has — if the mount doesn't appear, try an absolute path.

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

4. **Verify the deny rule actually holds.** Try to write a dummy file inside the mounted `agentic` path (then clean it up), and confirm it's blocked. `settings.json` hot-reloads mid-session, so a corrected rule can be re-probed without restarting. **Non-negotiable:** never accept a failed probe as expected behaviour — a correctly written deny rule does hold, so diagnose it against the two known failure modes below, and only if it still doesn't block, say so explicitly to the user and fall back to the split-authority discipline: draft changes from the project session, apply them from a session whose working directory is `agentic` itself.
   - **The rule is a `Write(...)` rule.** File-permission checks match only `Edit(path)` rules; `Write(...)` matches nothing. Rewrite as `Edit(...)`.
   - **The path isn't anchored.** For paths outside the project root, only `~/`-rooted globs anchor: `Edit(../agentic/**)` and `Edit(**/agentic/**)` both fail to block, `Edit(~/**/agentic/**)` blocks. (Relative paths *inside* the project do work — the anchoring problem is specific to escaping the project root.)

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
