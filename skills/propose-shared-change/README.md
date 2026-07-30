# propose-shared-change — notes

## Where the shape came from

Two handoffs from `f1_fantasy`'s `fastf1_v1` effort, both real:

- **2026-07-27** — three proposals drafted from the project session, structured as gap / evidence / drop-in text / suggested placement. The structure held up under use and is what the skill now prescribes.
- **2026-07-28** — applying them from the `agentic` session caught one proposal that duplicated a clause and contradicted a rule in the very file it targeted. It landed as two edits, one of them narrowing the rule it contradicted, rather than the single append it was drafted as.

## Why the check sits on the receiving end

The reason is behavioural, not structural. A project session *can* read `agentic`: it is mounted read-only via `additionalDirectories`, and the deny rule covers only `Edit`. `f1_fantasy`'s `.claude/settings.json` was confirmed on 2026-07-30 to be configured exactly that way during both handoffs.

It nonetheless drafted against a file it had not read, because it was carrying project context rather than `agentic`'s. So the skill asks the sending session to read the target — cheap, and it was never impossible — but does not rely on it. The receiving session verifies regardless, because that is the session holding the target file open while editing, and it is where the evidence says the defect is actually caught.

An earlier framing in `learning/INBOX.md` justified the check by claiming the project session *cannot* read the target files. That was wrong on the mechanism, and worth not restoring: a non-negotiable resting on a false capability claim is one an agent will discount as soon as it notices it can read the file.

## Decisions

- **A skill rather than prose in `learning/CONVENTIONS.md`** (2026-07-30). The receiving-end check fires in a fresh `agentic` session, and `CONVENTIONS.md` is by its own rule not loaded at skill runtime — so prose there could not reach the half of the handoff that carries the weight.
- **Transport is `~/.claude/handoff/<project>-<YYYY-MM-DD>.md`** (2026-07-30), outside both repos and outside version control. Chosen over committing the file to the project's `docs/<effort-name>/`: it is transient by design, and committing it would introduce a new mount direction (`agentic` reading the project repo) that does not otherwise exist.
