---
name: propose-shared-change
description: Draft a change to agentic's shared conventions, skills, or agents from a project session, and verify and apply an incoming draft from an agentic session. Trigger when a project session spots generic guidance worth promoting, when a change is needed to a mounted read-only file, or when an agentic session is handed drafted proposals to place.
---

# Propose a shared change

The two-session handoff for changing `agentic` from a project repo, and for applying what arrives.

Split authority: a project session reads and proposes, never writes; edits and commits happen only from a session whose working directory is `agentic` itself. The two ends below run in different sessions — follow the one you are in.

## Sending — drafting from a project session

Write the proposals to `~/.claude/handoff/<project>-<YYYY-MM-DD>.md`, outside both repos so nothing lands in the wrong one, and tell the user the path. That is where this session's part ends.

Read the target file first. It is mounted read-only, so drafting blind is a choice, and it is how a proposal ends up restating or contradicting what the file already says.

One entry per proposal:

- **The gap** — what the shared instruction doesn't currently cover.
- **Evidence** — `file:line` pointers into this project showing where the gap actually bit. A proposal with no incident behind it is a hypothesis; label it as one.
- **Drop-in text** — the proposed wording, written to fit the target file's voice and conventions.
- **Suggested placement** — target file and section, offered for the receiving session to confirm.

**Non-negotiable:** never edit `agentic` from a project session, and never drop a proposal because you can't apply it yourself. Draft it and hand it over.

## Receiving — applying from an `agentic` session

**Non-negotiable:** check every proposal against what its target file already says before applying any of it. Both handoffs to date produced a proposal that duplicated a clause and contradicted a rule in the file it targeted. This check is what catches that.

Per proposal, decide and report:

- **Already covered** — say where, and drop it.
- **Contradicts the target** — the drafted text and the existing rule can't both stand. Resolve it with the user; the fix is often reshaping both, not appending one.
- **Lands as drafted** — apply it.
- **Lands reshaped** — say what changed and why. The sending session had no way to know.

Apply what survives as ordinary work, one change per commit. Delete the handoff file once every proposal in it is applied or declined.
