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
- Before committing: run available lint/typecheck/test.
- Before edits: `git status --short`.
- Required in every `.gitignore`: node_modules/, .env*, dist/, build/, .next/, .DS_Store (already present).

## Verification Discipline (critical)
When following docs/implementation-plan.md:
- After running any verification command listed in a phase's "Verification checklist", immediately update the corresponding [ ] → [x] in the plan.
- Do not mark a task complete based only on todo lists or memory.
- The checkboxes inside implementation-plan.md are the authoritative record.
- This rule applies for the entire duration of the project.

## Workflow
- Source of truth for development moved out of GoogleDrive FUSE (unreliable for active work).
- Use `~/Github/ISMS-ISO-toolkit` for all work.
- First push always uses `-u` on the feature branch.

## Future
When adding Python risk tool, Streamlit, Excel generators:
- Add proper tests.
- Update this file with build/test commands (e.g. `make`, `pytest`, `python -m`).

Initial content: planning README only.
