# Conventions

Settled decisions — repo structure, naming, workflow patterns. This is what eventually gets copied into a real repo.

## Tool-portability for agents/skills

Decided: future-proof now rather than defer. Canonical agent/skill content is written in a tool-agnostic format — plain markdown with minimal YAML frontmatter (`name`, `description` only, no tool-specific fields like Claude's `tools`/`model`) — so it can be read or adapted by any coding agent (Claude Code, Copilot, Cursor, etc.), not just Claude Code. Tool-specific integration (e.g. Claude Code discovering skills/agents via `/add-dir`) is handled by a thin adapter layer (symlinks) rather than by changing the canonical format. See the `agentic` repo's `agents/` and `skills/` folders for the applied structure.

## Authoring skills and agents: concise, non-negotiables signposted

Skill and agent instructions are read under context pressure and may be
summarised mid-task. Write them so the load-bearing parts survive.

- **Be concise.** Every sentence competes with the task for attention. Cut
  throat-clearing, non-actionable rationale, and examples a capable agent
  doesn't need. Aim for the shortest text that removes ambiguity, not a
  complete essay.
- **Signpost non-negotiables.** A rule that must not be dropped gets an
  explicit, greppable marker: a bold **Non-negotiable:** label on its own
  line, stated as a self-contained imperative that still makes sense with
  the surrounding prose stripped away. These are the lines that must survive
  compression — make them stand out.
- **Minimise duplication — extract shared instruction, don't copy.** Two
  kinds of "shared" pull in different directions. Settled *decisions* (the
  human-facing rationale and history) live in this CONVENTIONS.md, which is
  not loaded at skill runtime — don't make a skill depend on reading it.
  Shared *instruction that skills need at runtime* goes in a dedicated
  `shared/` folder, created only when the need actually arises and kept lean,
  with one file per concern so a skill can pull in just the relevant piece.
  If two skills need the same rule, extract it to `shared/` and have both
  reference it rather than duplicating.
- **Qualify cross-references by repo.** A skill may run inside a project repo
  with this repo mounted elsewhere, so a bare relative path is ambiguous.
  Name the repo in the reference — `agentic`'s `shared/persistent-docs.md`,
  not a bare `shared/persistent-docs.md`.
- **Be consistent.** Reuse the same section structure, vocabulary, and
  cross-reference style across skills, so familiarity with one transfers to
  the next.

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

Project repos (not this one) use a standard structure for requirements/plans/execution logs, so agents and humans always know where to look. Because skills need it at runtime, the structure itself lives in `shared/persistent-docs.md` — that file is the source of truth for the mechanics; this section records only the decision to adopt it.

Scaffolding a new effort folder, and reviewing existing docs in a repo for migration to this structure, is handled by the `init-project-docs` skill (report/propose only — it never moves files automatically).

## Test-driven development: encouraged where behavior is known upfront

Default to test-first — write a failing test, then implement — when the expected behavior is already clear: pure logic, bug fixes (regression test before the fix), APIs with a defined contract. Skip test-first for exploratory/prototype work, UI layout, or anything where the shape of the solution is still being discovered — write tests after, once the design settles, or skip entirely for throwaway exploration.

Applies to project repos with actual code — this repo itself has no code/build/test tooling (per `CLAUDE.md`).
