# Stage 0: Foundation

## Goal

Build a minimal foundation that can be cloned, checked, and extended on local Linux, GPU server, and Aliyun.

## Required Outputs

- Repository folders for docs, environment templates, configs, scripts, harness, experiments, and knowledge.
- Environment check script.
- Minimal harness case and runner.
- Experiment template.
- Tests for the harness runner and environment check script.

## Acceptance Checks

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
python3 harness/runners/run_echo.py \
  --cases harness/cases/minimal_echo.jsonl \
  --report harness/reports/minimal_echo_report.md
```

Passing Stage 0 means these commands work on at least one Linux machine and the machine notes explain what must be checked on the next machine.

## Completion Log

Record after implementation:

```text
Date: 2026-06-29
Commit: 26c9709
Machine: zoukai-Default-string
Environment check: PASS - bash scripts/check/check_environment.sh
Unit tests: PASS - python3 -m unittest discover -s tests -v, 4 tests
Minimal harness: PASS - cases=2 failed=0
Notes: Secret scan and placeholder scan returned no matches.
```
