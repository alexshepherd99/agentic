# Agentic engineering topics to explore

## Proposals from bbmon — drafted, awaiting a decision

Five proposals handed over via `propose-shared-change` between 2026-08-17 and 2026-08-31, moved here on 2026-08-31 and the handoff files deleted. Each carries its drop-in text verbatim, so applying one needs nothing else. All five were re-checked against their targets on 2026-08-31 and none had been applied. Listed in the priority order Alex set; not a queue to work through in one session — one change, one commit, per `propose-shared-change`'s receiving rule, which also requires checking each proposal against what its target file already says before applying any of it.

### 1. The security review never reads the code — `skills/review-repo-security/SKILL.md`

**The gap.** The skill reads every blob as *text* — pattern scans and a semantic pass — and never reads any of it as *logic*. That scope is defensible; nothing in the file says so, so a completed review reports "clean" and the word carries a claim the review never tested. Sharpest where the review touches an effort doc's recorded controls: confirming that `plan.md` lists CSRF, a host allowlist and a sandboxed root unit is evidence about the *record*, and the report's voice doesn't distinguish that from evidence about the code.

**Evidence** (bbmon, 2026-08-31). A full run completed all nine steps and reported clean; of the 15 controls in that project's plan it verified none in code — only that they were written down, and it called the unauthenticated admin page's compensating controls "documented decisions, not gaps". The user asked whether the code had been reviewed; it hadn't. The code review that followed found a passwordless route from the deploy account to root: `scripts/bootstrap.sh` chowns the install tree to the deploy account, a root systemd unit executes a Python interpreter out of that same tree, and a passwordless `systemctl restart` grant completes it — defeating a boundary the project's own access doc claims. Every file involved is unremarkable text; the finding exists only in the relationship between three of them. It also found CSV formula injection in the web export path. The built-in `/security-review` was tried and failed on `origin/HEAD` being unset; on a clean tree it would have read nothing, which is the diff-scoped limitation `SKILL.md:8` already states.

**Drop-in text** — a new section between the `correct-repo-exposure` paragraph that closes `## Reviewing` and the existing `## Before a risky change`:

```markdown
## After the review — the code itself

This skill reads the repository as *text*. None of it is read as *logic*, and a
report that does not say so lets "clean" carry a claim the review never tested.

**Non-negotiable: say which question you answered.** Controls recorded in an
effort doc are evidence about the record. Confirming a plan lists a control is
not confirming the code implements it, and the two are easy to write in the same
voice.

Then suggest a code review as its own session, on the cadence rule above: say
what prompted it and let the user schedule it. **Not in this session** — the
rule that keeps this review out of implementation work keeps a code review out
of this one.

Name what it would cover, because the difference is not obvious:

- Input reaching a subprocess, the filesystem, or SQL. Argument injection as
  well as shell injection — an argv list stops the second and not the first.
- Privileged paths: what runs as root, and **who can write the code it runs**. A
  root unit executing from a directory the deploy account owns is a passwordless
  route to root, and it is invisible to any scan of file contents because it
  lives in the relationship between files.
- Output leaving in a format another program executes — CSV formulas, and
  anything rendered as HTML rather than as text.
- Whether the claimed controls are in the code at all: authentication, CSRF,
  escaping, and bounds on anything caller-supplied.

The built-in `security-review` does not cover this either, for the reason at the
top of this file: it is diff-scoped, so on a clean tree it reads nothing.
```

**Also to decide.** Whether the frontmatter description should say the skill covers *exposure* rather than security in general — "exposed credentials, machine or personal identifying data, and weakened controls" is accurate, and is precisely what let that session read the skill as complete. Deliberately not settled by the proposal: whether the code review deserves a skill of its own. The sender didn't create one — the section above is enough to start a session and `coding-standards` already carries the review-time posture. Reconsider if a third project hits the same gap.

### 2. The superseded-text convention is contested by the repo that used it — `shared/persistent-docs.md:22`

**The gap.** `persistent-docs.md:22-24` requires superseded content to keep its original wording under a dated `[Superseded YYYY-MM-DD: …]` marker, "not rewritten or deleted". bbmon does the opposite, deliberately, and has since 2026-08-05: the annotated `requirements.md` was rejected on review because it left a reader holding two contradictory statements and working out which was current, and git history already provides the recovery the marker protects. bbmon now deletes the stale text and puts the reasoning in the append-only log. The shared file doesn't acknowledge that the choice exists, so every session on that project meets a convention its own repo contradicts.

**Evidence.** `bbmon/docs/phase-1/log.md:44-46` — "Superseded text is deleted here, not annotated" — plus that repo's auto-memory, both recording it as a deliberate divergence "not yet proposed back". It never was: the shared convention stood unchallenged from 2026-08-05 to 2026-08-30 while the only repo applying it did the opposite. It reached `agentic` only because proposal 3 below edits the bullet immediately beneath it. Second instance of a proposal parked in per-project memory — see the retrospective-trigger bullet in *Longer-term* below.

**Drop-in text** — as a sub-bullet under `:22`:

```markdown
  - Where a project finds the marker does more harm than good — two contradictory statements in front of a reader who has to work out which is current — rewriting cleanly is a legitimate project-level choice, recorded in that project's own `CLAUDE.md`, with git history providing the recovery this rule protects. `log.md` stays append-only either way.
```

**This is a conversation, not an edit.** Three outcomes are live: the convention changes, it gains the opt-out above, or it stands with bbmon as a documented exception and bbmon conforms. The sending session explicitly declined to pick, and route the decision through `propose-shared-change` so the target file's existing content gets checked either way. If bbmon is the one to change, its `CLAUDE.md` and its auto-memory both need correcting.

### 3. A long-running effort's log needs a roll point — `shared/persistent-docs.md:13` and `:25`

**The gap.** `:13` says logs are curated prose and explains what to put in them; `:25` says `log.md` is append-only. Between them they describe how one entry is written and forbid editing old ones, and say nothing about what happens when a single effort runs long enough that nobody reads the file any more. The justification for curating the prose is that the log carries reasoning worth keeping — if the file stops being opened, the curation buys nothing.

**Evidence.** `bbmon/docs/phase-1/log.md` is 987 lines, ~17,000 words, 26 entries over 27 days — one effort, still in progress, with no natural end before the effort ends. The 2026-08-30 session's own orientation is the finding: asked "what's next", it read `BACKLOG.md` and `plan.md` in full and then `tail -120` of the log, never opening lines 1–867. A decision recorded only there is a decision no later session sees — and item 2 above is the worked example, sitting at line 44 of that file and going unproposed for 25 days. The repo had already worked around this by hand: `plan.md` carries "Decisions taken with this plan", "Open items" and the gate sections — the durable half of the log, lifted out and maintained separately, by habit rather than by instruction.

**Drop-in text.** Replace the bullet at `:13` — unchanged except for a new final sub-bullet:

```markdown
- **Logs are curated prose, not a transcript.** Record the decision, the outcome, and the reasoning — not raw command output.
  - Quote output only where the exact text is the point (an error message, a surprising value), and then only the lines that carry it.
  - Reporting *in session* is different: quoting a real failure there is expected. This governs what lands in the file.
  - **A decision is recorded in `plan.md` or `requirements.md`, not only in the log.** The log says what happened on a day; those two say what is true now. Anything a later session must not have to re-litigate goes into one of them when it is settled — the log narrates a decision, it does not store it.
```

Replace the sub-bullet at `:25` with these two:

```markdown
  - `log.md` is append-only — correct it with a new entry, never by editing an old one.
  - **A long effort rolls its log.** When a milestone or gate closes, move its entries and everything older into `log-archive.md`, leaving the current milestone's in `log.md`. Nothing is rewritten and nothing is deleted: the text is identical, in a file beside it.
    - The trigger is mechanical on purpose. Entries move because their milestone is finished, never because someone judged they would not be wanted again — that judgement is a prediction, and a wrong one buries the reasoning you turn out to need.
    - The archive is not read on orientation. A session reads `requirements.md`, `plan.md` and the current `log.md`, and opens the archive only when investigating something specific. That is what the roll is for.
    - Roll only once the log has grown past the point where it is read end to end. A short effort never needs to.
```

Net change is about six lines, deliberately reshaping the two bullets that already exist rather than adding a "log lifecycle" section — the concern raised alongside it is that the shared guidance is outgrowing what actually gets followed. Left unsettled on purpose: whether `log-archive.md` should itself be split when an effort has many milestones. No project has hit it.

### 4. Close the session when the work is finished, instead of proposing the next piece — `shared/collaboration-workflow.md`

**The gap.** `:16` covers *unrelated* work — "a separate session: capture it durably and offer to close" — and makes audits and retrospectives sessions of their own. Nothing covers the *related* next piece: the next milestone, the next backlog item, the obvious follow-up in the same effort, which is the far more common continuation. The end-of-session review at `:33` lists three checks and then stops, saying nothing about what to do once they pass, so the file reads as permission to carry on. The result is a session that keeps going because the assistant keeps offering, and the drift and context loss `:16` exists to prevent arrive by the route it doesn't cover.

**Evidence** — behavioural, from a session transcript rather than a file. bbmon's M4 was finished, committed, pushed and summarised, and the summary ended "Next is the hardware: G2 and G3 clear on one visit"; nothing had asked for that. Alex, unprompted, in that session: "I like to avoid long sprawling sessions and prefer starting a fresh session when a piece of development is finished... at the moment, you tend to suggest more work, or the next development item, when a given chunk of work is done." The *durable* half is already covered — every entry in bbmon's log ends by naming what comes next, and `persistent-docs.md:5` puts not-yet-started work in `BACKLOG.md` — so only the conversational nudge needs stopping, and the drafted text draws that line explicitly.

**Drop-in text** — its own top-level bullet immediately after **End-of-session review** (`:33-36`), the rule it hands off from:

```markdown
- **When the work is finished, recommend a fresh session rather than the next piece of work.** Say the piece is done, say what would come next, and leave it there. Don't offer to start it, and don't end on a question whose easy answer is "yes, carry on".
  - "Finished" is the whole of what was asked, judged against the definition-of-done clauses in `how-we-work` — not the first item of a multi-part request, and not a convenient pause.
  - **Non-negotiable:** what comes next is still written down — `BACKLOG.md`, the effort's `log.md`, a memory. Ending the conversation is not ending the record.
  - A long session drifts and loses context; the next piece starts better from the durable record than from a summary of a summary. The user asking for more in the same session settles it — this governs what you volunteer.
```

**Two things to weigh.** `collaboration-workflow.md` is already over `file_max_words` on the `hygiene-ok` override at `:3`, and this adds ~120 words — a flag never blocks, but the override's rationale may want re-dating, or this may be the nudge to split the file. And the rule could misfire as licence to stop early, mid-task; the "Finished is the whole of what was asked" boundary is what holds that, and is the clause to keep if the text gets trimmed. The offered alternative was to fold it into **End-of-session review** as a fourth sub-bullet; the sender didn't draft it that way because the triggers differ — the review fires on "a session with nontrivial back-and-forth", while this has to fire whenever the work is done, including after a small piece with no back-and-forth at all.

### 5. Mutation testing needs a restore that works on untracked files — `skills/coding-standards/SKILL.md`

**The gap.** The Testing section makes mutation testing non-negotiable where red-first is impossible, and names as one of the two cases a brand-new function whose only pre-implementation red is an import failure. It says to break the implementation, watch it go red, and name the mutation when reporting — and says nothing about restoring the file between mutations. The obvious reflex, `git checkout <file>`, is silently wrong for exactly that case: new code is usually untracked when it's mutated, git can't restore a path it has never seen, so the mutation stays, the next one lands on top of it, and every result after the first measures a file broken in ways the report doesn't mention. The failure is quiet in a specific way: each round still prints "1 failed, 7 passed", which is what a correct round looks like.

**Evidence.** bbmon, 2026-08-28: five mutations against a then-untracked `retention.py` with `git checkout` as the restore step. The restore failed every time, so B–E stacked on A; the results looked plausible and were reported before the stacking was noticed, then withdrawn and re-run with a file copy. On the honest second run, one mutation that had appeared to be caught was **not** caught, exposing a real defect in the test. So the cost wasn't just wasted effort — the broken harness produced a false "this test catches that mutation" result, which is the one claim mutation testing exists to establish. It bit again on 2026-08-30, when a session mutated a brand-new untracked `web/export.py` and `git checkout --` would have deleted it rather than restored it.

**Drop-in text** — a third sub-bullet under "When red-first is impossible, verify by mutation", after the pure-refactor sub-bullet, since it applies to both cases above it:

```markdown
  - **Restore from a copy, never `git checkout`, and confirm the suite is green again between mutations.** The case this bullet exists for is usually new code, and `git checkout` cannot restore a file git does not yet track — the restore fails, the mutation stays, and the next one lands on top of it, so every result after the first is void while each round still prints the one-failure shape that a correct round has. Copy the file aside before the first mutation and restore from the copy; a green suite between mutations is what proves the baseline came back.
```

Smaller version, if instruction volume is the greater concern — append one clause to the existing "name the mutation and quote the failure when reporting" line instead:

```markdown
… name the mutation and quote the failure when reporting, restoring from a file copy rather than `git checkout`, which cannot undo a mutation to code git does not yet track.
```

The sub-bullet buys two things the clause doesn't: the "confirm green between mutations" check, which is the step that actually catches a failed restore, and the explanation of why the failure is invisible. If neither is worth the length, the clause alone still closes the trap.

## Immediate — needed to start using skills on future projects

### Topic: Define size and structure metrics for instruction content

**Status**: settled and running, 2026-07-29 to 2026-07-30. `shared/instruction-hygiene.md` holds the thresholds and triage rules, `tools/instruction_hygiene.py` computes them with a stdlib `unittest` suite beside it, and `tools/README.md` records every derivation and source. Runs as an end-of-session step in `agentic` only, prints a one-line outcome, and flags but never blocks. How it got here is in the commits; what follows is what is still open.

Two decisions worth not re-deriving. `CONVENTIONS.md` gets no entry for this — the thresholds and their rationale already live in the two files above. And the standing `duplication` flags stay exactly as they are: verified benign (the consistency convention working correctly), not overridden because a `duplication` override is file-wide and would blind both files to real duplication later, and not silenced by raising the n-gram size from 8 to 11 — every shared run in the corpus is exactly 10 tokens, so 11 would be fitted to them and would blind the check to a real 10-token match. Two flags, one cause: `grill-me`/`init-project-docs` citing `shared/persistent-docs.md` (confirmed 2026-07-30), and `onboard-project`/`reconcile-project-instructions` stating the same "run from a session in the project repo, with `agentic` reachable" precondition, present since the 2026-08-10 split and confirmed 2026-08-16 — each skill loads on its own trigger, so each has to state its own precondition, and `reconcile` already defers the mechanics rather than repeating them. Don't re-propose either, and don't reword one to clear the flag.

Remaining:

- **Two metrics move mechanically under splitting** — the prescribed fix for a long block is to split it into bullets, and `count_instructions` counts every bullet, so this triage moved `instruction_count` 73 → 98 (+34%) while clearing 7 block flags. `nonneg_max_density_pct` is the mirror case: a ratio whose denominator is the block count, so any split lowers it regardless of content — it cleared here purely as a side effect. Both need a different unit, or an explicit note that they track splitting rather than quality.
  - Sharpest instance, 2026-08-16: deleting a sub-bullet from `collaboration-workflow.md` raised density 25% → 26%, and adding the `hygiene-ok` comment on the same edit took it back to 25% — because `blocks()` counts the comment. A marker the shared doc calls "metadata, not instruction" moved the ratio, in the direction that silences the check. The denominator counts text that carries no rule at all, which is a stronger argument for a new unit than the splitting cases above.
- **The em dash counts as a word** — `" — ".split()` yields `"—"`. Same family as the label-fusion and list-marker defects fixed earlier on 2026-07-30. Largely defused by the move to 42: it no longer decides any flag. It does still inflate every count by one per dash, and the 41 → 46 gap the threshold was derived from would shift slightly if fixed, so re-derive rather than just patching the tokenizer.
- **Nothing implements the enumeration check** — the shared doc listed four zero-tolerance defects, but only `duplication`, `dangling_reference` and `runtime_reachability` exist. The four enumerating files found on 2026-07-29 were found by hand. The doc now states the gap; decide whether to build the check or drop the claim.
- **Decide whether a block should count its list marker** — `sentence_max_words` now ignores `- `, `block_max_words` still counts it, so the same text is measured two ways. Changing it shifts every list block by one word, which means revisiting the derivation (cluster 59–64, jump to 81) rather than just the code.
- **Make the check runnable from a project repo** — it resolves thresholds relative to the repo root, so a project session can't run it against its own `CLAUDE.md`. Until then the end-of-session step sits only in `agentic`'s `CLAUDE.md`, not the shared workflow, and `review-repo-health` degrades to applying the thresholds by reading when it runs in a project repo.

## Longer-term — investigate later

- Mocking should be confined to API boundaries — file, OS, time, randomness — never internal code. Would need a repo test review to check/enforce.
- Caveman-talk skill: a terser response style to save tokens.
- Tools that minimize tool output (e.g. test runs, git status) to just what is needed, rather than dumping everything.
- Refine tests so that only the useful tests get written.
- Skills discipline: add counter-cases to a skill to catch bad behaviour, not just positive instructions.
- For any given skill: what am I asking it that the agent doesn't already know? If nothing, is the skill adding value, or could it be better expressed as a series of counter-cases for the agent to avoid?
- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use. One concrete instance landed 2026-08-16 as the `review-repo-health` skill — on-demand, dedicated session, report-only. What stays open is everything that isn't a review the human calls for: whether improvement should also arrive continuously, and from where.
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger. Datapoint (`fastf1_v1`, 2026-07-27): three instruction proposals surfaced from a scheduled end-of-effort consistency review, not noticed in passing — and one of them had been sitting in that project's per-project memory the whole time, where no other project could benefit from it. Suggests the trigger wants to be an explicit step in an effort's plan, and that it should include sweeping per-project memories for anything general enough to promote.
- Review the skills built in this repo against what already exists — Claude Code's built-in skills/commands, Anthropic's published skills, and skills shared across the broader internet — to spot overlap, gaps, and ideas worth borrowing. Approach TBD (how to discover and compare against external skill sets isn't figured out yet).
- **`git -C <repo> worktree add <relative-path>` resolves the path against the repo, not the cwd** — hit 2026-08-03 while running the hygiene tool against a base commit for comparison: the worktree landed at the repo root as an untracked `base/`, caught in `git status` before the push. The generic trap is that `-C` rebases *every* relative path in the command, so a path meant for the scratchpad silently lands in the repo — which is precisely what the scratchpad convention exists to prevent. Decide whether one incident is enough to encode (an "absolute paths with `git -C`" line in `coding-standards` or the collaboration workflow) or whether it stays here as a known gotcha.
- Revisit `INBOX.md`'s own conventions. Its title ("topics to explore") doesn't cover drafted, ready-to-apply edits, and parking three of them here in 2026-07 pushed the file past `CLAUDE.md`'s ~1,500-word cap purely on entries designed to be deleted as soon as they landed (they did, on 2026-07-28, taking it back to ~850). Decide whether long drafted text belongs somewhere else entirely — say `proposals/`, one file per proposal — with the INBOX holding only a pointer. The related question of whether a word cap on a queue measures anything useful was settled 2026-07-29: queue and project-local docs are out of scope for the hygiene metrics, so this file has no cap.

- **Strip out the size-optimising behaviour for logs and instruction files.** Two parts. (1) When revised text replaces old text, just replace it — no dated annotation or superseded marker unless specifically asked for one; overlaps bbmon proposals 2 and 3 above, so settle them together. (2) Streamline instruction files loaded every session (e.g. an effort's `plan.md`) by moving superfluous detail into an archive file that isn't read by default. Raised 2026-09-28.

## Considered and deliberately not proposed

Surfaced by `f1_fantasy`'s `fastf1_v1` handoff (2026-07-27) alongside the three instruction edits that landed, but judged not worth promoting. Kept so the same observations don't get re-raised from scratch; line references are to that repo's `docs/fastf1_v1/log.md` at commit `95c6bc0`.

- **Check third-party assumptions against reality before writing code** — the FastF1 `EventSchedule` pickle round-trip check (`log.md:309-313`) and the selective-session-load equivalence check (`log.md:113`) both de-risked a change before any code was written. Real, but reads as ordinary care rather than a rule that would change an agent's behaviour.
- **An entrypoint no test exercises will drift silently** — `log.md:371-384`, on deleting `scripts/get_fastf1_data.py` after it drifted twice without a red test. Already captured concretely in `f1_fantasy`'s `BACKLOG.md` ("No test exercises any script's `__main__` block"), which exists to decide the standard; generalising it now would pre-empt that decision.

Surfaced by the bbmon handoff (2026-08-15) and deliberately not proposed. Kept so they don't get re-raised.

- **A commit-provenance ledger under `~/.claude/projects/<project>/`**, designed 2026-08-13 and not built. Once `gc.reflogExpire` is `never` the reflog *is* that ledger — git appends it, with no hook and no per-commit habit — so it landed instead as a step in `review-repo-security` on 2026-08-16, with the expiry setting in `publish-repo-safely`'s baseline. Also rejected on the way: comparing the branch against `origin`, which any pull silently empties. Neither form survives a machine change — a reflog is clone-local, and signed commits are the record that travels.
- **A "non-negotiables index" file**, considered as a decay control against rules being forgotten deep into a long session. Rejected: it is another always-on file that duplicates every rule it indexes, and the duplication check would flag it correctly.
- **Splitting an instruction file purely to clear `file_max_words`.** Both halves load together, so it saves no context and only moves the score. Split when it improves findability instead. This decided the `coding-standards` question on 2026-08-15, where the split turned out to be unnecessary anyway — the hygiene tool strips fenced code before counting, and `wc -w` does not.
- **Trimming instruction text to reduce context.** The always-on tier measured ~1,281 words on 2026-08-15. Word-shaving there is not where the leverage is; routing rules to the tier they belong in, and keeping sessions from sprawling, are.

Surfaced by a `/doctor prompt-audit` run (2026-10-03) as low-confidence flags and deliberately left in place. Kept so the next audit's flags are recognised, not re-weighed.

- **"Both handoffs to date" in `skills/propose-shared-change/SKILL.md`** — dated phrasing, but it is the evidence behind the receiving-side non-negotiable, and a reason is context, not cruft.
- **"the 2026-07 full-repo pass" in `skills/review-repo-health/SKILL.md`** — a dated origin, but it is what each seed rests on; the skill's own seeding rule judges new seeds against that same standard.
