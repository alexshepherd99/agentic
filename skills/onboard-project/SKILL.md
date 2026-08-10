---
name: onboard-project
description: Set up a project repo to consume this repo's (agentic's) shared agents/skills and conventions read-only. Trigger when the user asks to onboard a project, wire up agentic, set up access to shared skills/conventions, connect a project repo to the agentic repo.
---

# Onboard Project

Wires a project repo up to consume `agentic`'s `agents/`/`skills/`/conventions read-only. This skill is the source of truth for the mechanics.

Run this from a session in the project repo, with `agentic` reachable — launched via `claude --add-dir ../agentic`.

## Steps

1. **Capture the path in both forms it's needed in.** Find where `agentic` sits relative to the project repo (commonly `../agentic`, but confirm — don't assume). Two consumers, two forms, not interchangeable:
   - **Relative** (e.g. `../agentic`) — for `additionalDirectories` (step 2), the launcher (step 3) and the `CLAUDE.md` pointer prose (step 4), where it reads as "where the mount is".
   - **Home-rooted glob** — literally `~/**/agentic/**`, for the deny rule (step 2). Deny rules only anchor against `~/`-rooted paths; a relative or unanchored path silently matches nothing.
     - Keep the `**` wildcard rather than substituting the real checkout path — it stays committable (no username, no assumed layout) and still resolves to "an `agentic` repo somewhere under `$HOME`".
     - If `agentic` lives outside `$HOME`, this won't match — root the glob at wherever it does live, and lean on step 5 to confirm.

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

3. **Commit a launcher script.** `additionalDirectories` grants tool access to the mount but does not load `agentic`'s skills or agents — only `--add-dir` does, and a bare `claude` gives no sign they're missing.

   Write `claude.sh` at the project root, `chmod +x` it, and commit it with the executable bit set:
   ```bash
   #!/usr/bin/env bash
   # Launch Claude Code with the shared `agentic` repo mounted, so its
   # skills and agents load. Relative paths only — nothing
   # machine-specific is committed.
   set -euo pipefail

   cd "$(dirname "$0")"

   agentic_dir="<relative-path-to-agentic>"

   if [ ! -d "$agentic_dir" ]; then
       echo "error: no agentic repo at $agentic_dir (expected beside this repo)" >&2
       exit 1
   fi

   exec claude --add-dir "$agentic_dir" "$@"
   ```
   Use step 1's relative path verbatim. The `README.md` beside this file explains why the script is shaped this way.

4. **Add a short pointer section to the project's `CLAUDE.md`:**
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

   Propose changes to `agentic` with the **`propose-shared-change`**
   skill — it defines how a draft crosses from this session to one
   that can write to `agentic`.
   ```
   Keep it a pointer, not a copy — don't duplicate `agentic`'s conventions content into the project. **Non-negotiable:** name the always-apply skills (`how-we-work`, `coding-standards`) explicitly — a plain mounted guidance file is easy to silently ignore, so the pointer is the backstop that surfaces them.

5. **Verify the deny rule actually holds.** Try to write a dummy file inside the mounted `agentic` path, then clean it up and confirm the mounted repo is clean again — an unblocked probe leaves a real file there.

   `settings.json` hot-reloads mid-session, but not instantly: a probe fired right after step 2 writes it can beat the reload, and that race is a likelier reason for a first miss than a malformed rule.

   **Non-negotiable:** re-probe once before diagnosing anything, and never accept a *second* failed probe as expected behaviour. A correctly written deny rule does hold once loaded, so diagnose a second failure against the two known failure modes below.
   - **The rule is a `Write(...)` rule.** File-permission checks match only `Edit(path)` rules; `Write(...)` matches nothing. Rewrite as `Edit(...)`.
   - **The path isn't anchored.** For paths outside the project root, only `~/`-rooted globs anchor: `Edit(../agentic/**)` and `Edit(**/agentic/**)` both fail to block, `Edit(~/**/agentic/**)` blocks. (Relative paths *inside* the project do work — the anchoring problem is specific to escaping the project root.)

   Only if it still doesn't block, say so explicitly to the user and fall back to the discipline itself, which stands on intent regardless of enforcement — the `propose-shared-change` skill holds it.

6. **Verify the launcher.** Run `./claude.sh` and confirm `how-we-work` is in the session's available skills. A bare `claude` in the same repo will not show it — that difference is the check, and it is the whole reason the script is committed.

7. **Report back** what changed (settings.json diff, launcher, CLAUDE.md addition, verification results) rather than assuming silent success.

## Staleness

The pointer section is static prose, written once. If `agentic`'s structure changes significantly later, re-run this skill to refresh it — there's no automatic sync.

## Next step

If the repo already has agent instructions of its own, run `reconcile-project-instructions` to reduce them to project-specific deltas.

Recommend running the `init-project-docs` skill to scaffold the project's own persistent-document structure (`BACKLOG.md`, `docs/<effort-name>/`) — a separate concern, kept separate so neither skill grows too large.

Also run `check-secret-scanning` to confirm the remote's credential controls are on.
