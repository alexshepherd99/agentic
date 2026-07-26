# Agentic engineering topics to explore

## Immediate — needed to start using skills on future projects

### Topic: Make test-first enforceable in `coding-standards` (+ `how-we-work`)

Tighten the Testing section of `skills/coding-standards/SKILL.md` (currently 2
bullets, lines 36-39) so test-first is enforceable rather than aspirational,
with a matching tweak to the definition-of-done bullet in
`skills/how-we-work/SKILL.md` (line 17).

**Evidence** (f1_fantasy, 2026-07-26): a session followed the current guidance
and still shipped a test that passed against the bug it covered. Widening an
exception handler that missed `zipfile.BadZipFile`; the first test wrote
arbitrary bytes to a fake spreadsheet, pandas raised `ValueError`, which the
*old* handler already caught — green test, untouched defect. Only running it and
expecting red exposed it. Truncating a real file reproduced the bug. The same
session patched a first-party function (`load_odds`) in a conftest fixture for
isolation; the cleaner fix was making the real boundary injectable.

Three gaps in the current bullet: it never says to *run* the test and observe
the failure; it says nothing about an unexpected pass (the signal the test is
wrong, easily misread as "already handled"); and nothing makes compliance
visible afterwards — a finished diff looks identical whether tests came first or
last.

**Proposed Testing section** (a proposal, not a prescription — review on merit):

- **Test-first where behaviour is known upfront.** Write the test, run it, and
  see it fail *for the reason you expect*, then implement — for pure logic, bug
  fixes, and APIs with a defined contract. The failing run is the point: a test
  never observed red proves only that it passes, not that it can fail.
- **Check the failure, not just the exit code.** A test failing with
  `ImportError`, `NameError` or a typo has demonstrated nothing about
  behaviour. Red means the assertion you care about failed.
- **An unexpected pass is a defect in the test, not a shortcut.** If a new test
  passes before the implementation exists, stop and diagnose: it is almost
  always exercising a different path from the one you mean to change. Rewrite it
  until it fails for the intended reason.
- **Prove a regression guard against the unfixed code.** When covering a latent
  or already-diagnosed bug, revert or stash the fix, confirm the guard fails,
  then restore. A guard never seen failing is decoration.
- **Report the red-green transition** when presenting the work — what failed and
  how. It is the evidence the test has power, and it cannot be recovered from
  the diff later.
- **Skipping test-first is a decision to state, not a default to assume.** For
  exploratory or throwaway work, say so and say why. "The change is obvious" is
  not a reason; it is the usual rationalisation, and small additive changes are
  where the discipline slips first.
- Avoid mocking existing first-party functions where a real call is practical —
  mock at genuine boundaries, not internal code you own. If isolating a test
  seems to need a first-party function patched, prefer making the real boundary
  injectable (a path, client or clock parameter) over patching the function.

**Proposed `how-we-work` change** — qualify green by having been red:

> **Definition of done: a green suite, reached from a red one.** In a repo with
> tests, confirm the relevant tests pass before starting a change, that each
> behavioural change was observed failing before it passed, and that the full
> suite is green before marking work complete.

**Judge before applying:**

- Seven bullets may be too long for a section that has to stay readable —
  weigh against the **Be concise** rule in `learning/CONVENTIONS.md`
  ("shortest text that removes ambiguity"). Candidate merge: the
  failure-message and unexpected-pass bullets.
- Does "report the red-green transition" belong in `coding-standards`, or in
  `how-we-work` with the other communication rules?
- Check the tightened wording against `learning/CONVENTIONS.md` (line 49
  describes the skill as "test-first-where-behaviour-is-known" — may need
  updating to match).

**Status**: queued, not started

### Topic: Build a manually-run repo-review skill

Turn the periodic repo review (done manually this session) into a reusable, manually-invoked skill, usable both in this repo and in project repos (mounted via the standard share). It should audit the repo for gaps, inconsistencies, drift / stale cross-references, duplication, and sprawl, and surface suggestions for the human to weigh — report/propose only, never act without sign-off (cf. `init-project-docs`).

Keep it open-ended, not a fixed checklist: the agent should recommend what's worth reviewing based on what it actually finds, rather than mechanically walking a prescriptive list. A short set of standing prompts (sprawl caps, dangling references, duplication, docs-vs-reality drift) can seed it, but the agent should stay free to raise anything else it notices.

Validated by the one-off full-repo pass (2026-07): stale cross-references (a doc pointing elsewhere for content that isn't there), structure/overview docs missing a folder that exists, entry/front-door docs that never state what the thing is, the same discipline duplicated across an always-loaded doc and a skill, and unclear relationships between adjacent sibling sections.

One concrete instance of the "introspection process for gradually improving the repo" item under Longer-term below.

**Status**: queued, not started

## Longer-term — investigate later

- Managing context + gated, documented steps with fresh context per step; consistency/coherence checks across docs, code, comments, tests after major chunks
- Multi-language repo — Python first, others possibly later
- Claude Code managing git — explore different levels of autonomy (commit-directly-to-main settled for the `agentic` repo specifically — broader question of auto-push, conflict handling, etc. still open)
- Introspection process for gradually improving the repo over time to be easier for agents to follow/modify/use
- Graphify (or similar) for encoding a project for agent readability — worth it, and at what threshold
- Encouraging the agent to refine its own instructions — post-project retrospective trigger
- Review the skills built in this repo against what already exists — Claude Code's built-in skills/commands, Anthropic's published skills, and skills shared across the broader internet — to spot overlap, gaps, and ideas worth borrowing. Approach TBD (how to discover and compare against external skill sets isn't figured out yet).
