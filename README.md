# agentic

## Onboarding a new project repo

To let a project repo use this repo's `agents/`/`skills/` and conventions (read-only, never copied):

1. Position the project repo as a sibling directory to this one (so `../agentic` resolves), or adjust the relative path to match your layout.
2. Launch a Claude Code session in the project repo with this repo mounted read-only:
   ```bash
   claude --add-dir ../agentic
   ```
3. Ask Claude to onboard the repo (invokes the `onboard-project` skill), which will:
   - Add `additionalDirectories`/deny rules to the project's `.claude/settings.json` so the mount persists across sessions and stays read-only.
   - Add a short pointer section to the project's `CLAUDE.md` referencing this repo's conventions/skills.
   - Verify the deny rule actually blocks writes (a known Claude Code permissions quirk means `--add-dir` mounts don't always inherit deny rules reliably — see `learning/CONVENTIONS.md`).
4. Usually, follow up by running the `init-project-docs` skill to scaffold the project's own persistent-document structure (`BACKLOG.md`, `docs/<effort-name>/`). This is a separate concern from onboarding the mount — see `learning/CONVENTIONS.md` under "Persistent documents in project repos".

You can also do these steps by hand — see the exact `settings.json` block and split-authority workflow in `learning/CONVENTIONS.md` under "Sharing agents/skills into project repos".

**Note:** the project's `CLAUDE.md` pointer section is static prose written once at onboarding time. If this repo's structure changes significantly later, existing projects' pointer text won't auto-update — re-run onboarding if you want it refreshed.