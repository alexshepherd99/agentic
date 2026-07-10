# Conventions

Settled decisions — repo structure, naming, workflow patterns. This is what eventually gets copied into a real repo.

## Tool-portability for agents/skills

Decided: future-proof now rather than defer. Canonical agent/skill content is written in a tool-agnostic format — plain markdown with minimal YAML frontmatter (`name`, `description` only, no tool-specific fields like Claude's `tools`/`model`) — so it can be read or adapted by any coding agent (Claude Code, Copilot, Cursor, etc.), not just Claude Code. Tool-specific integration (e.g. Claude Code discovering skills/agents via `/add-dir`) is handled by a thin adapter layer (symlinks) rather than by changing the canonical format. See the `agentic` repo's `agents/` and `skills/` folders for the applied structure.
