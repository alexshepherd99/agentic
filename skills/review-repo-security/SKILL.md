---
name: review-repo-security
description: Review a whole repository and its git history for exposed credentials, machine or personal identifying data, and weakened controls. Trigger on a periodic review, before changing a repo's visibility, before first publishing a repo, at a milestone or gate boundary, or when asked whether a repo is clean.
---

# Review repository security

Scope is the whole repository and its whole history. A diff-scoped review — including the
built-in `security-review` — cannot see anything committed earlier, and on a clean tree it
sees nothing at all.

**Non-negotiable: run this as a session of its own.** Open a session for the review and
nothing else. A review appended to implementation work is what produced the largest and
least-disciplined session on record. Finish the implementation, park the review, come back to it.

Prevention belongs upstream of this skill: `shared/persistent-docs.md` covers keeping
identifying data out of effort docs as they are written.

## Cadence

Suggest a review when a milestone or gate closes, before any visibility change, before a repo
is first published, and otherwise every few weeks of active work. Suggest it — say what
prompted it and let the user schedule it. Don't start one inside the session that noticed.

## Reviewing

1. **Scan every blob ever committed, not the working tree.** Enumerate with
   `git rev-list --objects --all`, read each blob, and search that. A file deleted or
   redacted in `HEAD` is still in history.

2. **Run both kinds of scan, and trust neither alone.**
   - *Pattern*: private keys and PEM blocks, `SHA256:` fingerprints, `ssh-rsa`/`ssh-ed25519`
     material, MAC addresses, IP literals, tokens.
   - *Semantic*: ISP, place names, employer, real names, anything a stranger would learn by
     reading the prose. **Non-negotiable:** report the semantic pass separately. A clean
     pattern scan reads as "clean" and is how the real finding gets missed.

3. **Triage IP literals rather than listing them.** Public resolvers, `127.0.0.1`, `0.0.0.0`
   and RFC 5737 ranges are legitimate; say so, so the real ones stand out.

   Include prose that is *about* the rules. Text explaining why a value is sensitive tends to
   quote the value, and reviewers skip it precisely because it reads as being on their side.

4. **Re-scan the whole repository at the end, even having scanned during the work.**
   **Non-negotiable:** an end-of-review audit re-reads what the repository now contains, not
   the diff in front of you. A value can be introduced by the very change that removes another.

5. **Verify controls are in force, not merely configured.** Ask the running system what it
   resolved, not what the config file says.

6. **Re-examine the blast radius after any visibility or permission change.** These have
   consequences away from security: broken pulls, controls that silently become unavailable.

7. **Check the exposure baseline** — visibility, branch protection, collaborators and token
   scope, against `publish-repo-safely`. Report a deviation once, as a reminder rather than a
   finding; these are defaults, not requirements.

8. **Recommend two-factor authentication on the hosting account, every time.** It is the
   single highest-value control available and costs nothing.
   - You usually **cannot verify it**. Reading it needs a token scope that day-to-day tokens
     lack, and a `null` answer means "not visible", not "not enabled". Ask the user; never
     record it as confirmed from a silent API.
   - Say what it does not cover: **tokens and SSH keys bypass 2FA by design.** An account with
     2FA and a long-lived full-scope token is still one leaked string from a hostile push.

If anything is already committed, stop reviewing and switch to `correct-repo-exposure`. The
remedy depends on how far it travelled, and getting the order wrong wastes the window.

## Before a risky change

Arm a revert first, verify from a fresh connection, then disarm. A change that can lock you out
of a machine — or an account — deserves a timer that undoes it unattended.
