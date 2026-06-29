# ai-agent-lab

Personal AI engineering lab for learning Codex deeply, building AI agents, managing knowledge systems, evaluating workflows, and migrating the same setup across local Linux, GPU server, and Aliyun.

## Current Stage

Stage 0 builds the foundation:

- Repository structure for learning notes, experiments, harnesses, configs, and knowledge.
- Minimal environment check for Linux machines.
- Minimal harness that can run one reproducible case and produce a report.
- Templates for future stage experiments and Feynman-style reviews.

## Quick Start

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
python3 harness/runners/run_echo.py \
  --cases harness/cases/minimal_echo.jsonl \
  --report harness/reports/minimal_echo_report.md
```

## Repository Map

- `docs/`: roadmap, stage notes, learning notes, references, reviews, and Superpowers specs/plans.
- `env/`: environment templates and machine-specific migration notes.
- `configs/`: Codex, MCP, agent, and model configuration examples.
- `scripts/`: setup, sync, check, and run scripts.
- `harness/`: reusable evaluation cases, runners, metrics, and reports.
- `experiments/`: small tests and comparison experiments.
- `projects/`: stage projects that can later become standalone systems.
- `knowledge/`: personal knowledge base inbox, processed notes, and indexes.
- `tests/`: tests for scripts, harnesses, and projects.

## Rules

- Keep secrets, tokens, private keys, model weights, and large datasets out of Git.
- Every experiment must include inputs, run commands, outputs, and a short conclusion.
- Every new feature must include a focused test.
- Prefer portable Python 3 and shell scripts until a stage requires heavier tooling.
