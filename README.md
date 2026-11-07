# agentic

Two roles: a personal scratchpad for learning agentic engineering (under `learning/`), and the home for reusable agents and skills (`agents/`, `skills/`) that project repos pull in read-only rather than duplicating per-repo. See `CLAUDE.md` for the full picture.

## Onboarding a new project repo

Project repos use this repo's `agents/`/`skills/` read-only, never copied. Two steps happen by hand, before any skill can run:

1. Put the project repo beside this one, so `../agentic` resolves — or adjust the path to match your layout.
2. Start a Claude Code session in the project repo with this repo mounted:
   ```bash
   claude --add-dir ../agentic
   ```

Then ask Claude to onboard the repo. The `onboard-project` skill does the rest — settings, the launcher later sessions start from, the `CLAUDE.md` pointer, and checks that each works — and names the skills to run after it.