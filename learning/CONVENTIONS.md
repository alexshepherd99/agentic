# Conventions

Settled decisions — repo structure, naming, workflow patterns. This is what eventually gets copied into a real repo.

## Tool-portability for agents/skills

Decided: future-proof now rather than defer. Canonical agent/skill content is written in a tool-agnostic format — plain markdown with minimal YAML frontmatter (`name`, `description` only, no tool-specific fields like Claude's `tools`/`model`) — so it can be read or adapted by any coding agent (Claude Code, Copilot, Cursor, etc.), not just Claude Code. Tool-specific integration (e.g. Claude Code discovering skills/agents via `/add-dir`) is handled by a thin adapter layer (symlinks) rather than by changing the canonical format. See the `agentic` repo's `agents/` and `skills/` folders for the applied structure.

## Skill development: bespoke over framework

Build skills in-house rather than adopting external agentic frameworks. (Rationale: stay in control of pace and direction; avoid trend-chasing that pulls focus from your own goals.)

- New skill development may include an optional web search for established approaches. (Rationale: learn from others' work without being obligated to adopt it — intelligence gathering stays optional.)
- Claude Code notes interesting patterns it encounters during work into a running list. (Rationale: build an idea backlog on your own schedule, not because trends demand it.)
- Every developed skill documents its source links/influences. (Rationale: trace where ideas came from, stay honest about influences.)
- Skills are refreshed via manual prompt, not on an automatic cadence. (Rationale: reviews happen when you decide it's time, not on a surrendered schedule.)

## Sharing agents/skills into project repos

Project repos consume this repo's `agents/`/`skills/` read-only, via `--add-dir` and `additionalDirectories`, never by copying.

Project `.claude/settings.json`:
```json
{
  "permissions": {
    "additionalDirectories": ["../agentic"],
    "deny": ["Write(../agentic/**)", "Edit(../agentic/**)"]
  }
}
```
Example shell alias for launching project sessions (illustrative name, not fixed): `alias claude-project='claude --add-dir ../agentic'`

**Split authority:** a project session may read conventions/skills and propose changes, but must not write to this repo. Actual edits/commits only happen from a session whose working directory is this repo itself — run two sessions in parallel and hand text across manually.

**Verification caveat:** deny rules on `--add-dir`/`additionalDirectories` paths may not reliably hold in all Claude Code versions. Verify once per machine by asking a project session to edit a dummy file in the mounted repo. If the deny rule doesn't hold, the two-session discipline above is the real safeguard — the deny rule is a backstop, not a guarantee.

## Persistent documents in project repos

Project repos (not this one) use a standard structure for requirements/plans/execution logs, so agents and humans always know where to look:

- **`BACKLOG.md`** (top-level) — global list of not-yet-started work, freeform/manual, no fixed mechanics beyond "one file, one list."
- **`docs/<effort-name>/`** — created once an item is picked up off the backlog and work starts. Holds that effort's `requirements.md`, `plan.md`, and `log.md`.
- **Collapsing is fine for small efforts** — a trivial effort can skip separate files and just use `log.md` with inline `## Requirements` / `## Plan` sections instead. Split out into separate files once any one section gets unwieldy.

Scaffolding a new effort folder, and reviewing existing docs in a repo for migration to this structure, is handled by the `init-project-docs` skill (report/propose only — it never moves files automatically).
