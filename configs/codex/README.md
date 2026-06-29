# Codex Configuration Notes

This folder stores examples and conventions for Codex usage in this repository.

## Boundaries

- Repo-wide agent rules live in root `AGENTS.md`.
- Reusable workflows should become Skills only after they are repeated and validated.
- Prompt experiments belong in `experiments/stage-1/`.
- Secrets and personal account settings do not belong in this repository.

## Stage 0 Validation

Use Codex to run a repo check, then compare the result with manual command output:

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```
