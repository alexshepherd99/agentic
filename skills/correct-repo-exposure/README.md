# correct-repo-exposure — source & influences

Split deliberately from `review-repo-security` rather than living inside it. The trigger is
different — something has already landed, discovered at any moment and usually not during a
review — and a skill loaded to answer "is this repo clean?" is the wrong thing to be reading
when the answer is already no.

Every case in the body is from the `bbmon` remediation of 2026-08-13, including the two the
session got wrong at the time: the rewrite left four fresh copies of the data behind (a
pre-rewrite bundle, two blob dumps from scanning, and the `--replace-text` file, which holds the
values verbatim because a search pattern *is* the data) while the repository was reported clean;
and it invalidated every SHA in the repository, including two quoted in its own docs, after the
user had been told they would survive.
