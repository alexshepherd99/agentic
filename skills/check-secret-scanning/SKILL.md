---
name: check-secret-scanning
description: Verify a repo's server-side credential controls — GitHub secret scanning and push protection — are enabled, and report any existing alerts. Trigger when onboarding a repo, when asked whether secrets are being scanned or whether push protection is on, or when auditing an existing repo's security posture.
---

# Check secret scanning

Confirms the server-side control behind the credentials non-negotiable in `agentic`'s `shared/collaboration-workflow.md` is actually on. That rule covers intent; this checks the mechanism.

Run against any repo, at onboarding or any time after — already-onboarded repos are the ones most likely to have been missed.

## Steps

1. **Identify the remote.** `git remote -v`. Only GitHub remotes can be checked this way; for anything else (GitLab, self-hosted), say it wasn't checked rather than implying it passed.

2. **Query the status:**
   ```bash
   gh api repos/<owner>/<repo> --jq '{visibility, secret_scanning: .security_and_analysis.secret_scanning.status, push_protection: .security_and_analysis.secret_scanning_push_protection.status}'
   ```

3. **Interpret against visibility:**
   - **Public, both `enabled`** — correct. Check existing alerts: `gh api repos/<owner>/<repo>/secret-scanning/alerts --jq 'length'`.
   - **Public, either `disabled`** — free to enable, in Settings → Code security. Secret scanning must be on first; push protection cannot be enabled alone.
   - **Private** — these controls need paid GitHub Secret Protection. Report as unavailable, not as a gap the user failed to close.

4. **Report and offer.** State what you found and offer to enable it. **Non-negotiable:** don't enable it yourself — it's an outward-facing change to the user's account, and it's theirs to make.

## What this does not cover

A clean result means nothing matched GitHub's patterns. Custom-shaped tokens and non-credential data are outside its reach, and alerts backfill asynchronously after first enabling — a `0` immediately after is provisional.
