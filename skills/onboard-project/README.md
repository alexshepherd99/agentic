# onboard-project — notes

Rationale behind the wiring. Not needed to run the skill.

## `additionalDirectories` does not load skills

`additionalDirectories` grants tool access to a mounted directory. Putting that directory's skills and agents into the session is a separate thing, and only `--add-dir` does it. Measured from a consuming project repo on 2026-08-10, Claude Code 2.1.226, with the project's `.claude/settings.json` loaded in every case; the prompt asked only whether `how-we-work` was in the session's available skills:

| launch | shared skills loaded |
| --- | --- |
| `claude -p` (settings `additionalDirectories` only) | no |
| `claude -p --add-dir /abs/path/to/agentic` | yes |
| `claude -p --add-dir ../agentic` | yes |
| `claude -p --add-dir ../agentic/` | yes |

The failure is silent. Nothing announces that a session has no shared skills, and the fallback — reading `SKILL.md` by path — depends on the session noticing. In one consuming repo it didn't: two sessions logged nine `Unknown skill: how-we-work` errors, silently read the file by path instead, and never told the user, while `settings.json` and the `CLAUDE.md` pointer were both configured exactly as this skill prescribes. It surfaced only when the user asked directly. That incident is why the launcher is a committed file with its own verification step, rather than an invocation someone is expected to remember.

## Why a launcher script rather than a symlink

Skill discovery follows symlinks, so `.claude/skills` could point into the mounted repo instead. Probed the same day, in a scratch project under a bare `claude -p`:

| layout | discovered |
| --- | --- |
| `.claude/skills/<name>/SKILL.md` | yes |
| `.claude/skills/<group>/<name>/SKILL.md` | no — discovery does not recurse |
| `.claude/skills/<name>` symlinked outside the repo | yes |
| `.claude/skills` itself symlinked outside the repo | yes, all children |

Rejected on 2026-08-10 anyway. A committed symlink dangles in any clone with no sibling `agentic`, and it either claims the whole `.claude/skills` directory — leaving the project nowhere to put skills of its own — or needs one link per shared skill, maintained by hand forever. The launcher's directory check turns that same missing-sibling case into a loud failure, and leaves `.claude/skills` free.

## Why the script is shaped the way it is

`cd "$(dirname "$0")"` resolves step 1's relative path against the script rather than the caller's shell, which is what keeps the committed file machine-independent — and it starts the session at the repo root, where `CLAUDE.md` and `.claude/` live. `"$@"` forwards arguments, so `./claude.sh --resume` works. The directory check is the difference between a clone failing loudly and a session quietly missing every shared skill.
