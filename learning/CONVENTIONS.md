# Conventions

Settled decisions — repo structure, naming, workflow patterns. This is what eventually gets copied into a real repo.

## Tool-portability for agents/skills

Decided: future-proof now rather than defer. Canonical agent/skill content is tool-agnostic — plain markdown, no tool-specific frontmatter — so any coding agent (Claude Code, Copilot, Cursor) can read or adapt it, not just Claude Code. Tool-specific integration (e.g. Claude Code discovering skills/agents via `--add-dir`) is a thin adapter layer (symlinks), not a change to the canonical format. The concrete frontmatter spec (`name`/`description` only) lives in `agents/README.md` and `skills/README.md` — don't restate it here.

## Authoring skills and agents: concise, non-negotiables signposted

Skill and agent instructions are read under context pressure and may be summarised mid-task. Write them so the load-bearing parts survive.

- **Be concise.** Every sentence competes with the task for attention. Cut throat-clearing, non-actionable rationale, and examples a capable agent doesn't need. Aim for the shortest text that removes ambiguity, not a complete essay.
- **Signpost non-negotiables.** A rule that must not be dropped gets an explicit, greppable marker: a bold **Non-negotiable:** label on its own line, stated as a self-contained imperative that still makes sense with the surrounding prose stripped away. These are the lines that must survive compression — make them stand out.
- **Minimise duplication — extract shared instruction, don't copy.** Two kinds of "shared" pull in different directions. Settled *decisions* (the human-facing rationale and history) live in this CONVENTIONS.md, which is not loaded at skill runtime — don't make a skill depend on reading it. Shared *instruction that skills need at runtime* goes in a dedicated `shared/` folder, created only when the need actually arises and kept lean, with one file per concern so a skill can pull in just the relevant piece. If two skills need the same rule, extract it to `shared/` and have both reference it rather than duplicating.
- **Qualify cross-references by repo.** A skill may run inside a project repo with this repo mounted elsewhere, so a bare relative path is ambiguous. Name the repo in the reference — `agentic`'s `shared/persistent-docs.md`, not a bare `shared/persistent-docs.md`.
- **Keep meta out of the instruction file.** Source links, influences, and design rationale go in a skill-local `README.md`, not `SKILL.md` / `agent.md`. The instruction file is loaded into context at runtime, so anything not needed to *perform* the skill is pure noise there.
- **Be consistent.** Reuse the same section structure, vocabulary, and cross-reference style across skills, so familiarity with one transfers to the next.
- **One line per paragraph (repo-wide).** Write markdown soft-wrapped — one long line per paragraph or list item, no hard breaks mid-paragraph — for cleaner diffs. Applies to every markdown file in this repo, not just skills/agents.

## Skill development: bespoke over framework

Build skills in-house rather than adopting external agentic frameworks. (Rationale: stay in control of pace and direction; avoid trend-chasing that pulls focus from your own goals.)

- New skill development may include an optional web search for established approaches. (Rationale: learn from others' work without being obligated to adopt it — intelligence gathering stays optional.)
- Claude Code notes interesting patterns it encounters during work into a running list. (Rationale: build an idea backlog on your own schedule, not because trends demand it.)
- Every developed skill documents its source links/influences in its `README.md` (not `SKILL.md` — see the authoring convention above). (Rationale: trace where ideas came from, stay honest about influences.)
- Skills are refreshed via manual prompt, not on an automatic cadence. (Rationale: reviews happen when you decide it's time, not on a surrendered schedule.)

## Sharing agents/skills into project repos

Project repos consume this repo's `agents/`/`skills/` read-only, via `--add-dir` and `additionalDirectories`, never by copying. The exact `settings.json` permissions block and the onboarding steps live in the `onboard-project` skill — the source of truth for the mechanics; don't restate them here.

**Split authority:** a project session may read conventions/skills and propose changes, but must not write to this repo. Actual edits/commits only happen from a session whose working directory is this repo itself — run two sessions in parallel and hand text across manually.

**Verification caveat:** deny rules on `--add-dir`/`additionalDirectories` paths may not reliably hold in all Claude Code versions. Verify once per machine by asking a project session to edit a dummy file in the mounted repo. If the deny rule doesn't hold, the two-session discipline above is the real safeguard — the deny rule is a backstop, not a guarantee.

## Persistent documents in project repos

Project repos (not this one) use a standard structure for requirements/plans/execution logs, so agents and humans always know where to look. Because skills need it at runtime, the structure itself lives in `shared/persistent-docs.md` — that file is the source of truth for the mechanics; this section records only the decision to adopt it.

Scaffolding a new effort folder, and reviewing existing docs in a repo for migration to this structure, is handled by the `init-project-docs` skill (report/propose only — it never moves files automatically).

## Project-facing guidance lives in skills, not this file

Guidance for how an agent should *work in a project repo* — the collaboration workflow and the code-writing standards — is packaged as skills, not stated here, so it's surfaced by skill-triggering and not duplicated per project.

- **`how-we-work` skill** — the collaboration workflow (clarifying questions, propose-before-editing, commit-per-item, green-suite DoD, end-of-session review). Triggers at the very start of any piece of work. (This repo's own workflow variant stays in its `CLAUDE.md`.)
- **`coding-standards` skill** — how project code should be written, including test-first-where-behaviour-is-known. Triggers before writing/modifying code.

*Why skills, not plain files:* in a project session only the project's own `CLAUDE.md` and registered skills/agents surface automatically; a guidance file mounted via `--add-dir` loads only if something reads it, so it's easy to silently ignore. Skills self-surface via their trigger descriptions. The `onboard-project` skill also names these skills in the project's `CLAUDE.md` pointer as a backstop.
