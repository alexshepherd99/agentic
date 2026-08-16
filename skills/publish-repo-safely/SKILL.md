---
name: publish-repo-safely
description: Set a project repository's exposure baseline — visibility, branch protection, named collaborators, local clone settings, and how git access is authenticated — and run the checks required before a repository is made public for the first time. Trigger when creating or onboarding a repo, when changing its visibility, or before publishing it.
---

# Publish a repository safely

## The baseline

Default configuration for a project repository, unless there is a reason to differ:

- **Public.** It keeps branch protection available at no cost, lets deploy targets pull without storing a credential, and removes a class of secret-management problem entirely. It only works because nothing identifying is ever committed — the two decisions depend on each other.
- **Branch protection on**, at minimum blocking force-push and branch deletion.
- **Specific named collaborators.** Grant by name; never leave access broader than the people actually working on it.

Going private is legitimate, but it is a trade rather than an upgrade: on a free plan it removes branch protection and stops unauthenticated pulls, which usually means putting a credential on a deploy target that previously needed none. Say so when it is chosen.

## Git access

**Fine-grained tokens are the encouraged default** — scoped to named repositories, granted only the permissions actually used, and carrying an expiry. Classic tokens with broad `repo` scope can push anywhere the account can reach *and* alter repository settings, which includes switching off the branch protection meant to contain them.

This is a recommendation, not a requirement. Where a broad or non-expiring token is in use, say so once, explain what it widens, and leave the choice with the user. Do not repeat it.

Where a machine only needs to read one repository, a read-only deploy key is tighter than any token: it is scoped to that repository by construction and cannot push.

## The local clone

Set `gc.reflogExpire` and `gc.reflogExpireUnreachable` to `never` in each working clone. The reflog is the only local record of which commits this machine actually made, and `review-repo-security` audits commit provenance against it; on the defaults it expires at 90 days and that audit quietly decays.

This is per clone, not per repository — a new machine starts on the defaults, and no git mechanism copies a reflog across. The cost is that objects held only by a reflog entry, such as amended or rebased-out commits, stop being collected; a history rewrite must expire them explicitly, which `correct-repo-exposure` already covers.

## Before publishing for the first time

Making a repository public publishes its **whole history**, not its current state. Review before the switch, not after — afterwards there is nothing left to decide.

1. Run `review-repo-security` over the whole history, as its own session.
2. Where history holds identifying data, rewrite it first, following `correct-repo-exposure`. A redaction in `HEAD` achieves nothing here: anyone who clones gets the original blobs.
3. Only then change visibility, and re-check what the change enabled or broke.
