# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

### Topic: Import Copilot instructions, then package everything for project use

Two-part plan for a fresh session:

1. **Bring in Copilot instructions from a previous project.** Review them and convert whatever is generic/repo-agnostic (not tied to that specific project) into settled conventions in this repo's `CONVENTIONS.md`.
2. **Package everything for project consumption.** Once that's done, sweep everything in this repo that's meant for other projects to use but isn't already a skill (e.g. convention entries that are really guidance for how a project should behave, not just decisions about this repo) — turn each into whatever form actually fits: a skill, an agent, or a plain guidance file that project repos read. Form is flexible; the point is making it consumable, not just documented here.
3. **De-duplicate and re-split CONVENTIONS as part of this.** As guidance moves into skills/guidance files, CONVENTIONS should reference them once rather than restating, and can be split by concern — repo-internal mechanics vs. guidance that gets mounted into projects. CONVENTIONS is already growing (7 sections, ~1,100 words, still under the sprawl caps but trending up); this is where that gets addressed. See the dedicated de-duplication task below.

**Status**: queued, not started

### Topic: Project instructions should only hold project specifics

**Principle**: a project repo's own agent instructions (`CLAUDE.md`, `.github/copilot-instructions.md`, etc.) should contain only project-specific content. Anything generic/repo-agnostic belongs in this `agentic` repo instead (as a convention or skill), not duplicated per-project.

**Action needed**: as part of repo setup, any existing Copilot/agent instructions in a project repo should be reviewed against this principle:
- Flag generic content that should be migrated out to `agentic` (convention/skill), rather than left duplicated in the project's own instructions.
- Flag inconsistencies between what the project's instructions say and what's already settled in `agentic`'s `CONVENTIONS.md`/skills.

Likely lands as a review step added to the `onboard-project` skill, once the "Import Copilot instructions" work above has happened and there's real content to test the review against.

**Status**: queued, not started — related to the topic above

### Topic: De-duplicate CONVENTIONS against skills/guidance once written

Once a rule has been coded into a skill or guidance file, CONVENTIONS should reference it once rather than restating it. Known instances to resolve when this runs:
- The `.claude/settings.json` permissions block is duplicated in CONVENTIONS ("Sharing agents/skills into project repos") and the `onboard-project` skill — CONVENTIONS should point at the skill.
- Clarifying-questions guidance overlaps CONVENTIONS ("Collaboration workflow (coding projects)") and the `grill-me` skill.

Ties into the "package everything for project use" topic above (the CONVENTIONS split is part of that).

**Status**: queued, not started

### Topic: Build a manually-run repo-review skill

Turn the periodic repo review (done manually this session) into a reusable, manually-invoked skill, usable both in this repo and in project repos (mounted via the standard share). It should audit the repo for gaps, inconsistencies, drift / stale cross-references, duplication, and sprawl, and surface suggestions for the human to weigh — report/propose only, never act without sign-off (cf. `init-project-docs`).

Keep it open-ended, not a fixed checklist: the agent should recommend what's worth reviewing based on what it actually finds, rather than mechanically walking a prescriptive list. A short set of standing prompts (sprawl caps, dangling references, duplication, docs-vs-reality drift) can seed it, but the agent should stay free to raise anything else it notices.

One concrete instance of the "introspection process for gradually improving the repo" item under Longer-term below.

**Status**: queued, not started

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger
