# CLAUDE.md — ISMS-ISO-toolkit

## Project
ISMS / ISO 27001 toolkit: risk register automation, Annex A gap analysis, policy templates, control mapping for Sec-CV portfolio.

## New project decision (per global CLAUDE.md)
**Should CLAUDE.md and docs/ be committed to this repo?**
**Yes.** CLAUDE.md is committed for workflow consistency, branch rules, git hygiene, and future agent instructions. docs/ (when added) should also be tracked.

## Git rules (mandatory)
- Always work on a feature branch. Never commit/push directly to `main`.
- Branch naming: `feat/<kebab>`, `fix/<kebab>`, `chore/<kebab>`.
- Atomic commits: one logical change per commit.
- Before committing: run available lint/typecheck/test (none yet).
- Before edits: `git status --short`.
- Required in every `.gitignore`: node_modules/, .env*, dist/, build/, .next/, .DS_Store (already present).

## Workflow
- Source of truth for development moved out of GoogleDrive FUSE (unreliable for active work).
- Use `~/Github/ISMS-ISO-toolkit` for all work.
- First push always uses `-u` on the feature branch.

## Future
When adding Python risk tool, Streamlit, Excel generators:
- Add proper tests.
- Update this file with build/test commands (e.g. `make`, `pytest`, `python -m`).

Initial content: planning README only.
