# Collaboration workflow

The repo-agnostic working discipline for any piece of work, from first mention to done.

- **Ask before assuming.** When scope or requirements are ambiguous, ask several small, scoped questions rather than one open-ended one, and prefer asking over guessing. **Non-negotiable:** don't build on unstated assumptions. For larger or underspecified requests, use the `grill-me` skill to pressure-test the request and the plan first.
- **Propose before writing.** For any non-trivial or judgment-call change, present the approach — or the concrete diff/draft — and get confirmation before editing. Review-then-write, not write-then-revise. Trivial one-line fixes are exempt.
- **Prefer the simplest solution.** When developing or changing a skill, agent, or instruction file, propose the smallest mechanism that meets the need. **Non-negotiable:** before proposing anything larger, state what it buys over the smaller version; if that can't be stated, propose the smaller one.
  - Complexity arrives by accretion during a session, not by decision — each addition looks reasonable against the previous draft. Compare against the smallest version that works, not against the draft in front of you.
- **Make every content change visible.** Author file content through `Write`/`Edit`, never shell redirection or an inline rewrite script. **Non-negotiable:** if you composed the content, `Write`/`Edit` it.
  - `Bash` output goes to the assistant and is not guaranteed to reach the human, so a shell write lands with no diff to review — and because the assistant *can* see that output, nothing feels wrong from its side.
  - Appending to a file is not an exception — read the tail and `Edit`, or `Write` the whole file; a repetitive rename is `Edit` with `replace_all`, not a rewrite loop.
  - The line is authorship, not mechanism: `Bash` remains right for running things (tests, git, greps, builds) and for file changes a *tool* authors — a formatter rewriting files, generated artifacts, `git rm`, redirecting a command's real output into a file.
- **One change at a time, commit per item.** Work a multi-item task in an agreed order (flagging dependencies), committing each resolved item on its own with a descriptive message before starting the next. Don't batch unrelated changes into one commit.
- **Never commit a credential.** **Non-negotiable:** no credential enters a commit, and one that reached a remote is rotated, not just reverted.
  - Covers API keys, tokens, passwords, and private keys, in code or quoted into a doc, a log, or a commit message. Placeholders and `.env.example` are fine; real values never are.
  - Every repo, not just public ones — visibility changes, and clones don't un-clone.
  - Rotating means issue a replacement *and* revoke the old value at the provider; a new key does not disable the old one.
  - Reverting or rewriting history is not a fix, and doing it first wastes the window that matters. Forks, existing clones, and cached views keep the value regardless.
- **Never commit data that identifies a machine, network, person, or place.** **Non-negotiable:** addresses, host key fingerprints, hostnames, MAC addresses, machine-specific paths, ISP, location, employer and real names stay out of the repo, in every visibility setting.
  - Judge the category, not the individual value. Debating each value is how the rule erodes.
  - **A pattern scan passing is not evidence.** Greps find addresses and key material; they do not find "our ISP" written in prose.
  - Unlike a credential, this cannot be rotated — `review-repo-security` and `correct-repo-exposure` carry the review and the remedy.
- **Propose improvements to shared instructions.** When you spot a better practice mid-work, propose an update to the relevant convention, skill, or instructions file — propose, don't silently apply.
  - If the target sits in a read-only mounted repo, the draft has to cross sessions to land: use `agentic`'s `propose-shared-change` skill rather than inventing a route.
- **Don't let a measurement claim more than it can carry.** When a change is justified by numbers, state what the comparison can and cannot distinguish before stating what it shows. **Non-negotiable:** a change that measured neutral is written up as neutral; "no measurable cost" is not "an improvement", and the correctness or simplicity argument for it has to stand on its own.
  - A delta smaller than its own run-to-run spread is not evidence.
  - A handful of races, runs or trials usually cannot separate the options being weighed.
- **End-of-session review.** Near the end of a session with nontrivial back-and-forth, check that:
  - everything discussed landed somewhere durable;
  - no doc still frames a since-resolved decision as open;
  - the working tree is clean and pushed.
