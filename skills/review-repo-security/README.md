# review-repo-security — source & influences

Prompted by a whole-repository security review of `bbmon` on 2026-08-13, which found what a
diff-scoped review structurally cannot: identifying data committed days earlier, a real routable
address used as a documentation example, and an sshd drop-in that was configured but not in
force.

The commit-provenance step arrives separately, from bbmon's exposure of 2026-08-15: `update.sh`
pulls `main` and runs it as root on the Pi, and branch protection is unavailable on a free-plan
private repo. It was parked as an always-on tripwire and re-decided on 2026-08-16 as a step here,
where a trigger already exists. No unexpected commit has ever appeared — the exposure is real and
so far hypothetical.

The standalone-session non-negotiable does not come from the review's own content. It comes from
the session-size evidence recorded at the top of `learning/INBOX.md` — that review was itself
run as the tail of an implementation session, and that session is the largest ever run on this
machine and one of only two to break an existing non-negotiable.
