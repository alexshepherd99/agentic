---
name: correct-repo-exposure
description: Drive the corrective action once something sensitive has already been committed — a credential, a key, or identifying data — including deciding whether to rewrite history and what a rewrite does not fix. Trigger the moment something sensitive is suspected to be in a commit or on a remote, or when a review finds one.
---

# Correct repository exposure

Preventing exposure is ordinary discipline; responding correctly once something has landed is where the damage is decided.

Pick by how far it has travelled. **Non-negotiable:** state which case applies and what it does not fix — never report a partial remedy as a fix.

- **Uncommitted** — edit the file. Nothing else needed.
- **Committed, not pushed** — the whole window worth having. Rewrite rather than delete forward: reset the commit, scrub, recommit, then expire unreachable reflog entries and garbage-collect. Confirm the old object is gone rather than assuming it.
- **Pushed** — assume it is public and stays public. Clones and caches do not un-clone.
  - *Credential*: rotate **first**, per the credentials non-negotiable in `shared/collaboration-workflow.md`. That is the only step that removes the attacker's capability. History rewriting is cleanup and does not substitute for it.
  - *Non-credential*: there is nothing to rotate. Decide deliberately whether to rewrite history, and record that disclosure already happened.
- **Any case** — redacting `HEAD` leaves history intact. If you did not rewrite history, say the data is still there.

## The remediation's own artifacts

**Non-negotiable:** delete them, and re-scan where they lived.

Removing data produces fresh copies of it: a backup bundle or branch taken before the rewrite, dumps of every blob made while scanning, and a replacements file that holds the values verbatim, because search patterns are the data.

Finishing the rewrite while those sit in a temp directory is the same partial remedy as redacting `HEAD` and calling it fixed.

## Before rewriting history

**Non-negotiable:** never rewrite history until the user has confirmed they understand what it does, in these terms:

- **every commit hash in the repository changes**, not only those after the edited commit. Any SHA quoted in docs, commit messages or issues stops resolving, so find and repoint them. A force-push is required;
- every other clone — other machines, deploy targets, collaborators — must be re-cloned or hard-reset, and will otherwise push the old history back;
- anything already published stays published. This prevents future disclosure; it does not undo past disclosure, and must never be described as if it did.

Get that confirmation explicitly. A rewrite is cheap in a single-collaborator repo and expensive in a shared one, and that judgement is the user's, not yours.

Do not soften exposure with "realistically nobody saw it". That is not evidence, and the person deciding needs the unhedged version.
