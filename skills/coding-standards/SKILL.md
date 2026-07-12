---
name: coding-standards
description: How project code should be written — simple design, small
  single-responsibility functions, meaningful names, documented public interfaces,
  explicit error handling (raise over silent None/sentinels), test-first where
  behaviour is known, and language-specific style (Python: PEP 8, type hints,
  fully-qualified imports, logging). Read BEFORE writing or modifying any source
  code, and when reviewing existing code.
---

# Coding standards (project code)

How code in a project repo should be written. Read before writing or changing source, and when reviewing existing code. (Language-agnostic unless a section says otherwise; Python is the current primary language.)

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

- **Test-first where behaviour is known upfront.** Write a failing test, then implement — for pure logic, bug fixes (regression test before the fix), and APIs with a defined contract. For exploratory/prototype/UI work where the solution's shape is still emerging, write tests after the design settles, or skip for throwaway exploration.
- Avoid mocking existing first-party functions where a real call is practical — mock at genuine boundaries, not internal code you own.

## Python-specific

Treat these as Python conventions, to be paralleled — not copied verbatim — for other languages later.

- Follow PEP 8.
- Use type hints for parameters and return values.
- Use fully-qualified module import paths; never relative imports.
- Use the standard `logging` module for errors and warnings, rather than ad-hoc prints.
