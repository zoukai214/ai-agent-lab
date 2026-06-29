# ai-agent-lab Agent Rules

## Project Purpose

This repository is a personal AI Agent engineering lab. It stores learning plans, notes, experiments, harnesses, configs, and stage projects for becoming an AI Agent engineer.

## Working Rules

- Use Chinese comments in code when comments are needed.
- Do not commit secrets, tokens, private keys, model weights, or large datasets.
- Do not modify build options such as `CMakeLists.txt` unless explicitly requested.
- New executable behavior needs a focused test.
- Prefer Python 3 standard library and Bash for Stage 0 infrastructure.
- Keep learning notes in `docs/`, experiments in `experiments/`, reusable evaluation code in `harness/`, and stage projects in `projects/`.

## Validation

Before considering a change complete, run:

```bash
python3 -m unittest discover -s tests
```

For environment changes, also run:

```bash
bash scripts/check/check_environment.sh
```
