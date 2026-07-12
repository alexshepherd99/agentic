# Coding standards (project code)

Generic, project-agnostic guidance for how code in a *project* repo should be written — distilled from prior projects' agent instructions. Staged here like everything in `learning/`; not yet a final source of truth.

This is distinct from `CONVENTIONS.md`, which records repo-structure and workflow *decisions*. Where the two overlap or conflict, `CONVENTIONS.md` wins. Applies to project repos with actual code — not this repo, which has no code/build/test tooling.

## Design and readability

- Prefer simple code; reach for established design patterns only where they genuinely fit, not by default.
- Keep functions small and focused on a single responsibility; use classes to group related data and behaviour.
- Use meaningful, descriptive names for variables and functions.
- Comment only where the logic isn't self-explanatory; let clear code carry the rest.
- Prioritise maintainability and readability over premature optimization.
- Preserve backward compatibility when modifying existing code, unless a breaking change is explicitly required.
- When reviewing or modifying existing code, read the relevant files fully to the end before changing them — don't act on a partial view.

## Public interfaces

- Document public functions, classes, and modules (docstrings, or the language's equivalent).
- Add type annotations to public parameters and return values where the language supports them.

## Error handling

- Handle exceptions explicitly at fallible boundaries: file I/O, data parsing, and external/API calls.
- Prefer raising exceptions over returning `None` or sentinel values for missing/invalid data, so failures are explicit rather than silent.
- Log context before raising, so an error carries enough information to debug.

## Testing

- Avoid mocking existing first-party functions where a real call is practical — mock at genuine boundaries, not internal code you own.
- (Whether to write tests first or after is governed by `CONVENTIONS.md`'s "Test-driven development" section.)

## Python-specific

Python is the current primary language; treat these as Python conventions, to be paralleled — not copied verbatim — for other languages later.

- Follow PEP 8.
- Use type hints for parameters and return values.
- Use fully-qualified module import paths; never relative imports.
- Use the standard `logging` module for errors and warnings, rather than ad-hoc prints.
