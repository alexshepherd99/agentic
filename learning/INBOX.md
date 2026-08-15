# Agentic engineering topics to explore

## Top of queue — a simple way to detect drift and propose parking

**Status**: parked 2026-08-15. The evidence is settled; the control is not. Nothing has been added to instruction content.

**What I actually want** is something *simple* that notices the session has moved off the topic it opened on and offers to stop. The proposal that came out of the bbmon handoff has become a very complex suggestion for that idea — a ~95-word non-negotiable in the always-on tier, with sub-bullets distinguishing parking from declining and the second topic from the length of the first. Come back and find the small version first: instruction text, a `SessionStart`-style hook, or something else. Don't apply the drafted text below just because it exists.

Drafted text, held (was **A1** of the bbmon handoff, targeting `shared/collaboration-workflow.md` after the "One change at a time" bullet):

```markdown
- **Park a topic that isn't the one the session started on.** When work arrives that is unrelated to the opening request, name it, write it to `BACKLOG.md` (or `agentic`'s `learning/INBOX.md`), and offer to close rather than carry both. **Non-negotiable:** a security review, a repo-wide audit, or an instruction retrospective is a session of its own, never a tail on implementation work.
  - Parking is not declining. The item keeps its evidence and gets a session with room to do it properly.
  - This is about the second topic, not the length of the first — finishing what you started is not drift.
```

**The evidence: session size predicts rule-breaks, and drift is what makes sessions oversized.** Measured 2026-08-15 across 46 non-trivial sessions on this machine (2026-07-21 to 08-14). Counting only sessions after the *"make every content change visible"* non-negotiable landed (2026-07-27 20:57), the only sessions that ever broke it were the two largest ever run — `bbmon/9eb71c9f` (291 assistant turns, 1 violation) and `bbmon/fc8a7175` (612 turns, 3) — while ~40 smaller post-rule sessions were clean. The oversized one opened with "let's start on m2" and then spent 21 of its 22 hours on an unrelated whole-repo security review.

- **Two false-positive traps will bite anyone re-running this.** The first pass reported 44 violations. ~30 predate the rule — the session with the most hits *ended* at 20:57 on 07-27, so it caused the rule rather than broke it — and ~10 are mutation testing, deliberately breaking finished code to watch a test go red, which `coding-standards` requires and which is exempt as a tool-authored change. The corrected count is 4.
- Sample is four events. A supported hypothesis, not a law.
- The open question the simple version has to answer: a rule this class of analysis keeps finding broken may want a hook rather than instruction text. A hook fires deterministically; instruction text depends on the session staying disciplined, which is what a 612-turn session stops doing.
- The analysis scripts (`session_stats.py`, `violations.py`, `session_detail.py`, `turns.py`, `find_heredoc.py`) sit in `~/.claude/handoff/`, outside version control. If the finding is worth re-measuring, promoting them into `tools/` is the follow-up; otherwise the numbers above are the record.

## Held — drafted, awaiting a session of their own

Both from the bbmon handoff of 2026-08-15 (its sections E1 and E2), held 2026-08-15. Both target the always-on tier and cannot be routed to a skill — their moment is "about to report", and no trigger fires there — and both were drafted in the final twenty minutes of a 22-hour drifted session, which is the condition the parked drift item at the top of this file exists to prevent. Holding is not declining; re-derive them in a session opened for the purpose.

### Definition of done, second clause: it has been run

Would target `skills/how-we-work/SKILL.md` (130 words, ample headroom), which defines done as a green suite reached from a red one. Nothing says code touching a real system must be executed against that system before it is called done.

Evidence, from bbmon's `docs/phase-1/log.md`: M1 lost buffered data on every SIGTERM; M3's parser could not read multi-line JSON from the real binary; M2's gate G1 found four (ping dead under the sandbox, non-zero exit after success, restart-everything-every-deploy, sshd drop-in silently inert); `update.sh`'s first run found two plus a regression at audit. **Nine defects, 193 passing tests, zero overlap.** All nine shared one shape — *reported success while not working* — which a suite cannot see, because it asserts on returned values rather than effects in the world.

```markdown
- **Definition of done, second clause: it has been run.** A green suite is evidence the logic
  is right, not that the thing works. Code that touches a real system — installers, service
  units, deploy scripts, anything shelling out or writing outside the process — is not done
  until it has been executed against that system.
  - **Non-negotiable:** when reporting work complete, name what has *not* been executed. "Tests
    pass" and "it runs" are different claims and must not be merged into one.
  - Where the real system is expensive or intermittent to reach, batch the checks rather than
    skipping them — see the gates convention in `shared/persistent-docs.md`.
```

The gates reference already resolves — that convention landed 2026-08-15.

### Verify the proposition you are claiming, not a neighbouring one

Would target `shared/collaboration-workflow.md`, after the measurement bullet. That bullet covers measurements; this covers verification claims generally, which is where the damage landed — the user acted on "I checked".

Four instances. The assistant stated both doc-quoted SHAs would survive a history rewrite and that it had checked; it had verified they were *ancestors of the edit point*, a true fact and the wrong proposition, and both broke. An M1 test asserted only that an error was raised, so the exploit executed and *then* failed validation, satisfying the assertion on its way past. Two M3 tests passed through a different path from the one they named. And the analysis that produced this handoff first reported 44 violations of the visible-changes rule: a regex had matched, the claim was that a rule had been broken, and the corrected count was 4.

```markdown
- **Verify the proposition you are about to claim.** **Non-negotiable:** before reporting something as checked, state what would have to be true for the claim to be false, and confirm the check would have caught that. A check that cannot fail is not verification.
  - The recurring failure is a check that tests something adjacent and true: confirming a commit is an ancestor is not confirming its hash survives a rewrite.
  - Say which of "I reasoned it" and "I ran it" applies. They are different claims and the reader is entitled to know which they are getting.
```

The handoff warned this tips `collaboration-workflow.md` over `file_max_words`. It no longer does: the parking rule was not applied, so the file sits at 696 body words and this addition lands near 776, inside the 800 cap. The file-splitting question is therefore not forced — take it up only if findability calls for it.

## Immediate — needed to start using skills on future projects

### Topic: Define size and structure metrics for instruction content

**Status**: settled and running, 2026-07-29 to 2026-07-30. `shared/instruction-hygiene.md` holds the thresholds and triage rules, `tools/instruction_hygiene.py` computes them with a stdlib `unittest` suite beside it, and `tools/README.md` records every derivation and source. Runs as an end-of-session step in `agentic` only, prints a one-line outcome, and flags but never blocks. How it got here is in the commits; what follows is what is still open.

Two decisions worth not re-deriving. `CONVENTIONS.md` gets no entry for this — the thresholds and their rationale already live in the two files above. And the one standing `duplication` flag, the citation of `shared/persistent-docs.md` shared by `grill-me` and `init-project-docs`, stays exactly as it is: verified benign (the consistency convention working correctly), not overridden because a `duplication` override is file-wide and would blind both files to real duplication later, and not silenced by raising the n-gram size from 8 to 11 — the corpus's longest shared run is 10 tokens, so with one data point there is no distribution to derive from and 11 would simply be fitted to it. Confirmed 2026-07-30; don't re-propose either.

Remaining:

- **Two metrics move mechanically under splitting** — the prescribed fix for a long block is to split it into bullets, and `count_instructions` counts every bullet, so this triage moved `instruction_count` 73 → 98 (+34%) while clearing 7 block flags. `nonneg_max_density_pct` is the mirror case: a ratio whose denominator is the block count, so any split lowers it regardless of content — it cleared here purely as a side effect. Both need a different unit, or an explicit note that they track splitting rather than quality.
- **The em dash counts as a word** — `" — ".split()` yields `"—"`. Same family as the label-fusion and list-marker defects fixed earlier on 2026-07-30. Largely defused by the move to 42: it no longer decides any flag. It does still inflate every count by one per dash, and the 41 → 46 gap the threshold was derived from would shift slightly if fixed, so re-derive rather than just patching the tokenizer.
- **Nothing implements the enumeration check** — the shared doc listed four zero-tolerance defects, but only `duplication`, `dangling_reference` and `runtime_reachability` exist. The four enumerating files found on 2026-07-29 were found by hand. The doc now states the gap; decide whether to build the check or drop the claim.
- **Decide whether a block should count its list marker** — `sentence_max_words` now ignores `- `, `block_max_words` still counts it, so the same text is measured two ways. Changing it shifts every list block by one word, which means revisiting the derivation (cluster 59–64, jump to 81) rather than just the code.
- **Make the check runnable from a project repo** — it resolves thresholds relative to the repo root, so a project session can't run it against its own `CLAUDE.md`. Until then the end-of-session step sits only in `agentic`'s `CLAUDE.md`, not the shared workflow.

### Topic: Build a manually-run repo-review skill

Turn the periodic repo review (done manually as a one-off in 2026-07) into a reusable, manually-invoked skill, usable both in this repo and in project repos (mounted via the standard share). It should audit the repo for gaps, inconsistencies, drift / stale cross-references, duplication, and sprawl, and surface suggestions for the human to weigh — report/propose only, never act without sign-off (cf. `init-project-docs`).

Keep it open-ended, not a fixed checklist: the agent should recommend what's worth reviewing based on what it actually finds, rather than mechanically walking a prescriptive list. A short set of standing prompts (sprawl caps, dangling references, duplication, docs-vs-reality drift) can seed it, but the agent should stay free to raise anything else it notices.

Validated by the one-off full-repo pass (2026-07): stale cross-references (a doc pointing elsewhere for content that isn't there), structure/overview docs missing a folder that exists, entry/front-door docs that never state what the thing is, the same discipline duplicated across an always-loaded doc and a skill, and unclear relationships between adjacent sibling sections.

One concrete instance of the "introspection process for gradually improving the repo" item under Longer-term below.

Scoped out (2026-07-30): checking an *incoming* proposal against what its target file already says belongs to the `propose-shared-change` skill, which makes it the receiving end's non-negotiable. This skill audits the repo as it stands; proposals in flight are the other skill's job.

Consumes the metrics item above: those thresholds are this skill's concrete seed checks, and the open-ended judgment pass is what this skill adds on top.

**Status**: queued, not started

## Longer-term — investigate later

- **Detecting a commit the session did not make** — parked 2026-08-15, was `check-commit-provenance` in the bbmon handoff. The exposure is real: `bbmon/scripts/update.sh` pulls `main` and runs it as root on the Pi, so a commit reaching `main` becomes root on a device, and branch protection is unavailable on a free-plan private repo. The container authenticates through one classic PAT with full `repo` scope, which can push to `main` *and* disable branch protection; 2FA does not constrain a token. Parked because no unexpected commit has ever appeared — the exposure is real but so far hypothetical.
  - **Not a skill.** Its trigger would be "the start of every session in a git repo, and after any pull", which is not a trigger, it is *always*. A skill would fire unreliably, and an unrun tripwire looks identical to a clean one. A `SessionStart` hook is the mechanism if it is ever built — it would be this repo's first hook, `.claude/settings.local.json` currently holding permissions only. Same open mechanism question as the drift item at the top of this file.
  - Design settled 2026-08-13, if it is built: the ledger lives under `~/.claude/projects/<project>/`, beside existing per-project state, and entries are appended by the session as it commits — no `post-commit` hook, so nothing to configure per machine.
  - It is a tripwire, not a control. Anyone with write access to the machine can edit the ledger; signed commits with a verified key are the cryptographic answer where the threat justifies it.
- Mocking should be confined to API boundaries — file, OS, time, randomness — never internal code. Would need a repo test review to check/enforce.
- Caveman-talk skill: a terser response style to save tokens.
- Tools that minimize tool output (e.g. test runs, git status) to just what is needed, rather than dumping everything.
- Refine tests so that only the useful tests get written.
- Skills discipline: add counter-cases to a skill to catch bad behaviour, not just positive instructions.
- For any given skill: what am I asking it that the agent doesn't already know? If nothing, is the skill adding value, or could it be better expressed as a series of counter-cases for the agent to avoid?
- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger. Datapoint (`fastf1_v1`, 2026-07-27): three instruction proposals surfaced from a scheduled end-of-effort consistency review, not noticed in passing — and one of them had been sitting in that project's per-project memory the whole time, where no other project could benefit from it. Suggests the trigger wants to be an explicit step in an effort's plan, and that it should include sweeping per-project memories for anything general enough to promote.
- Review the skills built in this repo against what already exists — Claude Code's built-in skills/commands, Anthropic's published skills, and skills shared across the broader internet — to spot overlap, gaps, and ideas worth borrowing. Approach TBD (how to discover and compare against external skill sets isn't figured out yet).
- **`git -C <repo> worktree add <relative-path>` resolves the path against the repo, not the cwd** — hit 2026-08-03 while running the hygiene tool against a base commit for comparison: the worktree landed at the repo root as an untracked `base/`, caught in `git status` before the push. The generic trap is that `-C` rebases *every* relative path in the command, so a path meant for the scratchpad silently lands in the repo — which is precisely what the scratchpad convention exists to prevent. Decide whether one incident is enough to encode (an "absolute paths with `git -C`" line in `coding-standards` or the collaboration workflow) or whether it stays here as a known gotcha.
- Revisit `INBOX.md`'s own conventions. Its title ("topics to explore") doesn't cover drafted, ready-to-apply edits, and parking three of them here in 2026-07 pushed the file past `CLAUDE.md`'s ~1,500-word cap purely on entries designed to be deleted as soon as they landed (they did, on 2026-07-28, taking it back to ~850). Decide whether long drafted text belongs somewhere else entirely — say `proposals/`, one file per proposal — with the INBOX holding only a pointer. The related question of whether a word cap on a queue measures anything useful was settled 2026-07-29: queue and project-local docs are out of scope for the hygiene metrics, so this file has no cap.

## Considered and deliberately not proposed

Surfaced by `f1_fantasy`'s `fastf1_v1` handoff (2026-07-27) alongside the three instruction edits that landed, but judged not worth promoting. Kept so the same observations don't get re-raised from scratch; line references are to that repo's `docs/fastf1_v1/log.md` at commit `95c6bc0`.

- **Check third-party assumptions against reality before writing code** — the FastF1 `EventSchedule` pickle round-trip check (`log.md:309-313`) and the selective-session-load equivalence check (`log.md:113`) both de-risked a change before any code was written. Real, but reads as ordinary care rather than a rule that would change an agent's behaviour.
- **An entrypoint no test exercises will drift silently** — `log.md:371-384`, on deleting `scripts/get_fastf1_data.py` after it drifted twice without a red test. Already captured concretely in `f1_fantasy`'s `BACKLOG.md` ("No test exercises any script's `__main__` block"), which exists to decide the standard; generalising it now would pre-empt that decision.

Surfaced by the bbmon handoff (2026-08-15) and deliberately not proposed. Kept so they don't get re-raised.

- **A "non-negotiables index" file**, considered as a decay control against rules being forgotten deep into a long session. Rejected: it is another always-on file that duplicates every rule it indexes, and the duplication check would flag it correctly.
- **Splitting an instruction file purely to clear `file_max_words`.** Both halves load together, so it saves no context and only moves the score. Split when it improves findability instead. This decided the `coding-standards` question on 2026-08-15, where the split turned out to be unnecessary anyway — the hygiene tool strips fenced code before counting, and `wc -w` does not.
- **Trimming instruction text to reduce context.** The always-on tier measured ~1,281 words on 2026-08-15. Word-shaving there is not where the leverage is; routing rules to the tier they belong in, and keeping sessions from sprawling, are.
