# Stage 0 Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan one task at a time. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the minimal, testable Stage 0 foundation for `ai-agent-lab`: repository structure, environment notes, experiment template, a tiny harness, and validation tests.

**Architecture:** Use one Git repository as the source of truth. Keep learning documents, environment templates, harness code, experiments, and knowledge assets in separate top-level folders so later stages can reuse them without moving files. Use Python standard library and shell scripts only for the first harness and checks to keep migration friction low across local Linux, GPU server, and Aliyun.

**Tech Stack:** Markdown, Bash, Python 3 standard library, `unittest`, Git.

---

## File Structure

- Modify: `README.md` to describe the lab purpose, Stage 0 quick start, and repository map.
- Create: `AGENTS.md` to preserve repo-local working rules for future Codex sessions.
- Create: `docs/roadmap/README.md` for the high-level learning map.
- Create: `docs/stages/stage-0-foundation.md` for Stage 0 goals and acceptance checks.
- Create: `env/templates/env.example` for non-secret environment variables.
- Create: `env/machines/local-linux.md`, `env/machines/gpu-server.md`, `env/machines/aliyun.md` for machine-specific notes.
- Create: `configs/codex/README.md` for Codex configuration conventions.
- Create: `scripts/check/check_environment.sh` for basic environment validation.
- Create: `harness/cases/minimal_echo.jsonl` for the first reproducible test case.
- Create: `harness/runners/run_echo.py` for the first tiny harness runner.
- Create: `harness/reports/README.md` to define report storage rules.
- Create: `experiments/000-template/README.md` for future experiment records.
- Create: `knowledge/inbox/README.md`, `knowledge/processed/README.md`, `knowledge/index/README.md` for the knowledge workflow.
- Create: `tests/harness/test_run_echo.py` to verify the harness runner.
- Create: `tests/scripts/test_check_environment.py` to verify the environment check script.

## Task 1: Repository Entry Points

**Files:**
- Modify: `README.md`
- Create: `AGENTS.md`

- [ ] **Step 1: Replace `README.md` with the Stage 0 overview**

````markdown
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
````

- [ ] **Step 2: Create `AGENTS.md`**

````markdown
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
````

- [ ] **Step 3: Review the rendered Markdown locally**

Run:

```bash
sed -n '1,220p' README.md
sed -n '1,220p' AGENTS.md
```

Expected: both files explain Stage 0, validation commands, and repo rules without placeholders.

- [ ] **Step 4: Commit**

```bash
git add README.md AGENTS.md
git commit -m "docs: define ai lab stage 0 entry points"
```

## Task 2: Stage 0 Documentation Skeleton

**Files:**
- Create: `docs/roadmap/README.md`
- Create: `docs/stages/stage-0-foundation.md`
- Create: `experiments/000-template/README.md`
- Create: `knowledge/inbox/README.md`
- Create: `knowledge/processed/README.md`
- Create: `knowledge/index/README.md`

- [ ] **Step 1: Create `docs/roadmap/README.md`**

```markdown
# AI Agent Learning Roadmap

This roadmap tracks the six-month path from Codex power user to AI Agent engineer.

## Stages

| Stage | Theme | Main Output |
| --- | --- | --- |
| 0 | Foundation | Portable repo structure, environment check, minimal harness |
| 1 | Codex Deep Usage | Codex workflow templates and AGENTS/Skill comparisons |
| 2 | Agent Principles | Minimal explainable agent and context/memory experiments |
| 3 | MCP and Knowledge | Searchable personal knowledge base prototype |
| 4 | Agent Engineering | Traceable workflow agent with observability |
| 5 | Advanced Systems | Self-hosted personal AI Agent platform prototype |

## Learning Rule

Each stage must produce a small test, a small project or reusable asset, a Feynman-style explanation, and a comparison conclusion.
```

- [ ] **Step 2: Create `docs/stages/stage-0-foundation.md`**

````markdown
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
````

- [ ] **Step 3: Create `experiments/000-template/README.md`**

```markdown
# Experiment Template

Copy this folder when starting a new experiment.

## Question

State the exact question being tested.

## Setup

- Machine:
- Date:
- Commit:
- Inputs:
- Command:

## Result

Record the observed output, report path, latency, cost if available, and failure notes.

## Conclusion

Summarize what changed, what did not change, and whether the result is reproducible.
```

- [ ] **Step 4: Create knowledge workflow README files**

Create `knowledge/inbox/README.md`:

```markdown
# Knowledge Inbox

Store raw links, notes, and source references here before processing.

Do not store private documents, secrets, large PDFs, or licensed datasets in Git.
```

Create `knowledge/processed/README.md`:

```markdown
# Processed Knowledge

Store cleaned notes, summaries, and Feynman-style explanations here.

Each processed note should link back to its source and include a short conclusion in your own words.
```

Create `knowledge/index/README.md`:

```markdown
# Knowledge Index

Store indexes, tags, source maps, and retrieval notes here.

The index should help future Codex, MCP, or RAG workflows find the right material quickly.
```

- [ ] **Step 5: Run Markdown content checks**

Run:

```bash
rg -n "TB[D]|TO[D]O|待[定]|占[位]" docs experiments knowledge
```

Expected: exit code 1 with no matches.

- [ ] **Step 6: Commit**

```bash
git add docs/roadmap/README.md docs/stages/stage-0-foundation.md experiments/000-template/README.md knowledge/inbox/README.md knowledge/processed/README.md knowledge/index/README.md
git commit -m "docs: add stage 0 learning skeleton"
```

## Task 3: Environment and Configuration Templates

**Files:**
- Create: `env/templates/env.example`
- Create: `env/machines/local-linux.md`
- Create: `env/machines/gpu-server.md`
- Create: `env/machines/aliyun.md`
- Create: `configs/codex/README.md`

- [ ] **Step 1: Create `env/templates/env.example`**

```dotenv
# Copy this file to a local, untracked .env file when needed.
# Keep real secrets out of Git.

AI_AGENT_LAB_ENV=local
AI_AGENT_LAB_MACHINE=local-linux
AI_AGENT_LAB_DATA_DIR=/tmp/ai-agent-lab-data
AI_AGENT_LAB_REPORT_DIR=harness/reports

# Optional proxy examples. Leave empty when not needed.
HTTP_PROXY=
HTTPS_PROXY=
ALL_PROXY=
```

- [ ] **Step 2: Create `env/machines/local-linux.md`**

````markdown
# Machine: local-linux

## Purpose

Daily learning, note writing, small experiments, and repository maintenance.

## Checks

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```

## Notes

- Record OS version with `lsb_release -a` or `cat /etc/os-release`.
- Record Python version with `python3 --version`.
- Record Git version with `git --version`.
````

- [ ] **Step 3: Create `env/machines/gpu-server.md`**

````markdown
# Machine: gpu-server

## Purpose

GPU-backed experiments, local model trials, and longer-running agent workflows.

## Checks

```bash
bash scripts/check/check_environment.sh
nvidia-smi
python3 -m unittest discover -s tests
```

## Notes

- Record GPU model and driver version from `nvidia-smi`.
- Keep model weights and datasets outside Git.
- Document any local path differences in an untracked `.env` file.
````

- [ ] **Step 4: Create `env/machines/aliyun.md`**

````markdown
# Machine: aliyun

## Purpose

Cloud migration checks, deployment experiments, and network comparison tests.

## Checks

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```

## Notes

- Record instance type, region, OS image, disk size, and network constraints.
- Keep cloud credentials outside Git.
- Compare command outputs with `local-linux` before changing scripts.
````

- [ ] **Step 5: Create `configs/codex/README.md`**

````markdown
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
````

- [ ] **Step 6: Run content checks**

Run:

```bash
rg -n "${AI_AGENT_LAB_SECRET_SCAN_PATTERN}" env configs
rg -n "TB[D]|TO[D]O|待[定]|占[位]" env configs
```

Expected: both commands exit 1 with no matches.

- [ ] **Step 7: Commit**

```bash
git add env/templates/env.example env/machines/local-linux.md env/machines/gpu-server.md env/machines/aliyun.md configs/codex/README.md
git commit -m "docs: add portable environment templates"
```

## Task 4: Environment Check Script with Tests

**Files:**
- Create: `scripts/check/check_environment.sh`
- Create: `tests/scripts/test_check_environment.py`

- [ ] **Step 1: Write the failing test**

```python
import os
import subprocess
import unittest
from pathlib import Path


class CheckEnvironmentScriptTest(unittest.TestCase):
    def test_script_reports_required_tools(self):
        repo_root = Path(__file__).resolve().parents[2]
        script = repo_root / "scripts" / "check" / "check_environment.sh"

        result = subprocess.run(
            ["bash", str(script)],
            cwd=repo_root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={**os.environ, "AI_AGENT_LAB_ENV": "test"},
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("ai-agent-lab environment check", result.stdout)
        self.assertIn("python3:", result.stdout)
        self.assertIn("git:", result.stdout)
        self.assertIn("repo:", result.stdout)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
python3 -m unittest tests.scripts.test_check_environment -v
```

Expected: FAIL because `scripts/check/check_environment.sh` does not exist.

- [ ] **Step 3: Create `scripts/check/check_environment.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "ai-agent-lab environment check"

if command -v python3 >/dev/null 2>&1; then
  echo "python3: $(python3 --version)"
else
  echo "python3: missing" >&2
  exit 1
fi

if command -v git >/dev/null 2>&1; then
  echo "git: $(git --version)"
else
  echo "git: missing" >&2
  exit 1
fi

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
echo "repo: ${repo_root}"
echo "env: ${AI_AGENT_LAB_ENV:-unset}"
echo "machine: ${AI_AGENT_LAB_MACHINE:-unset}"

if [ -f "${repo_root}/README.md" ]; then
  echo "README.md: present"
else
  echo "README.md: missing" >&2
  exit 1
fi
```

- [ ] **Step 4: Make the script executable**

Run:

```bash
chmod +x scripts/check/check_environment.sh
```

- [ ] **Step 5: Run test to verify it passes**

Run:

```bash
python3 -m unittest tests.scripts.test_check_environment -v
```

Expected: PASS.

- [ ] **Step 6: Run the script manually**

Run:

```bash
bash scripts/check/check_environment.sh
```

Expected: output includes `ai-agent-lab environment check`, `python3:`, `git:`, `repo:`, and `README.md: present`.

- [ ] **Step 7: Commit**

```bash
git add scripts/check/check_environment.sh tests/scripts/test_check_environment.py
git commit -m "test: validate environment check script"
```

## Task 5: Minimal Harness Runner with Tests

**Files:**
- Create: `harness/cases/minimal_echo.jsonl`
- Create: `harness/runners/run_echo.py`
- Create: `harness/reports/README.md`
- Create: `tests/harness/test_run_echo.py`

- [ ] **Step 1: Write the failing test**

```python
import json
import tempfile
import unittest
from pathlib import Path

from harness.runners.run_echo import load_cases, run_cases, write_markdown_report


class RunEchoHarnessTest(unittest.TestCase):
    def test_load_cases_reads_jsonl(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            cases_path = Path(tmp_dir) / "cases.jsonl"
            cases_path.write_text(
                json.dumps(
                    {
                        "id": "case-001",
                        "input": "hello",
                        "expected": "hello",
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            cases = load_cases(cases_path)

        self.assertEqual(len(cases), 1)
        self.assertEqual(cases[0]["id"], "case-001")
        self.assertEqual(cases[0]["input"], "hello")

    def test_run_cases_marks_pass_and_fail(self):
        cases = [
            {"id": "pass", "input": "same", "expected": "same"},
            {"id": "fail", "input": "actual", "expected": "expected"},
        ]

        results = run_cases(cases)

        self.assertEqual(results[0]["status"], "pass")
        self.assertEqual(results[1]["status"], "fail")
        self.assertEqual(results[1]["actual"], "actual")

    def test_write_markdown_report_contains_summary(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            report_path = Path(tmp_dir) / "report.md"
            write_markdown_report(
                report_path,
                [
                    {
                        "id": "case-001",
                        "input": "hello",
                        "expected": "hello",
                        "actual": "hello",
                        "status": "pass",
                    }
                ],
            )
            report = report_path.read_text(encoding="utf-8")

        self.assertIn("# Minimal Echo Harness Report", report)
        self.assertIn("Passed: 1", report)
        self.assertIn("| case-001 | pass |", report)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
python3 -m unittest tests.harness.test_run_echo -v
```

Expected: FAIL because `harness/runners/run_echo.py` does not exist.

- [ ] **Step 3: Create `harness/cases/minimal_echo.jsonl`**

```jsonl
{"id": "echo-001", "input": "Codex can use a harness.", "expected": "Codex can use a harness."}
{"id": "echo-002", "input": "Stage 0 checks reproducibility.", "expected": "Stage 0 checks reproducibility."}
```

- [ ] **Step 4: Create `harness/runners/run_echo.py`**

```python
#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_cases(cases_path):
    cases = []
    with Path(cases_path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            case = json.loads(stripped)
            for key in ("id", "input", "expected"):
                if key not in case:
                    raise ValueError(f"Missing key '{key}' in {cases_path}:{line_number}")
            cases.append(case)
    return cases


def run_cases(cases):
    results = []
    for case in cases:
        actual = case["input"]
        status = "pass" if actual == case["expected"] else "fail"
        results.append(
            {
                "id": case["id"],
                "input": case["input"],
                "expected": case["expected"],
                "actual": actual,
                "status": status,
            }
        )
    return results


def write_markdown_report(report_path, results):
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    passed = sum(1 for result in results if result["status"] == "pass")
    total = len(results)

    lines = [
        "# Minimal Echo Harness Report",
        "",
        f"Total: {total}",
        f"Passed: {passed}",
        f"Failed: {total - passed}",
        "",
        "| Case | Status | Expected | Actual |",
        "| --- | --- | --- | --- |",
    ]
    for result in results:
        lines.append(
            f"| {result['id']} | {result['status']} | {result['expected']} | {result['actual']} |"
        )
    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Run the minimal echo harness.")
    parser.add_argument("--cases", required=True, help="Path to a JSONL case file.")
    parser.add_argument("--report", required=True, help="Path to the Markdown report.")
    args = parser.parse_args()

    results = run_cases(load_cases(args.cases))
    write_markdown_report(args.report, results)

    failed = sum(1 for result in results if result["status"] == "fail")
    print(f"cases={len(results)} failed={failed} report={args.report}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Create `harness/reports/README.md`**

```markdown
# Harness Reports

Generated reports from harness runs can be stored here when they are small and useful for learning records.

Do not commit large logs, private data, model outputs containing secrets, or cost-heavy raw traces.
```

- [ ] **Step 6: Run test to verify it passes**

Run:

```bash
python3 -m unittest tests.harness.test_run_echo -v
```

Expected: PASS.

- [ ] **Step 7: Run the harness manually**

Run:

```bash
python3 harness/runners/run_echo.py \
  --cases harness/cases/minimal_echo.jsonl \
  --report harness/reports/minimal_echo_report.md
```

Expected: exit code 0 and output like:

```text
cases=2 failed=0 report=harness/reports/minimal_echo_report.md
```

- [ ] **Step 8: Inspect the report**

Run:

```bash
sed -n '1,120p' harness/reports/minimal_echo_report.md
```

Expected: the report contains total case count, pass count, fail count, and both case IDs.

- [ ] **Step 9: Commit**

```bash
git add harness/cases/minimal_echo.jsonl harness/runners/run_echo.py harness/reports/README.md harness/reports/minimal_echo_report.md tests/harness/test_run_echo.py
git commit -m "test: add minimal echo harness"
```

## Task 6: Full Stage 0 Validation

**Files:**
- Modify: no source files expected unless validation exposes a defect.

- [ ] **Step 1: Run all tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 2: Run environment check**

Run:

```bash
bash scripts/check/check_environment.sh
```

Expected: exit code 0 and output includes `python3:`, `git:`, and `README.md: present`.

- [ ] **Step 3: Run minimal harness**

Run:

```bash
python3 harness/runners/run_echo.py \
  --cases harness/cases/minimal_echo.jsonl \
  --report harness/reports/minimal_echo_report.md
```

Expected: exit code 0 and output includes `cases=2 failed=0`.

- [ ] **Step 4: Check for common secret patterns**

Run:

```bash
rg -n "${AI_AGENT_LAB_SECRET_SCAN_PATTERN}" .
```

Expected: exit code 1 with no matches.

- [ ] **Step 5: Check for placeholder markers**

Run:

```bash
rg -n "TB[D]|TO[D]O|待[定]|占[位]" README.md AGENTS.md docs env configs scripts harness experiments knowledge tests
```

Expected: exit code 1 with no matches.

- [ ] **Step 6: Commit validation fixes if any were required**

If any validation step required a source fix, commit only those fixes:

```bash
git add README.md AGENTS.md docs env configs scripts harness experiments knowledge tests
git commit -m "fix: complete stage 0 validation"
```

If no source fixes were required, do not create an empty commit.

## Task 7: Stage 0 Completion Review

**Files:**
- Modify: `docs/stages/stage-0-foundation.md`

- [ ] **Step 1: Add a completion log to `docs/stages/stage-0-foundation.md`**

Append:

````markdown

## Completion Log

Record after implementation:

```text
Date: 2026-06-29
Commit:
Machine:
Environment check:
Unit tests:
Minimal harness:
Notes:
```
````

- [ ] **Step 2: Fill the completion log with actual command outcomes**

Use the latest commit hash from:

```bash
git rev-parse --short HEAD
```

Use the machine name from:

```bash
hostname
```

Use the validation command outcomes from Task 6.

- [ ] **Step 3: Commit the completion review**

```bash
git add docs/stages/stage-0-foundation.md
git commit -m "docs: record stage 0 completion review"
```

## Self-Review

- Spec coverage: this plan covers Stage 0 repository structure, environment templates, machine notes, Codex config notes, check script, minimal harness, experiment template, knowledge workflow, and tests.
- Placeholder scan: the plan intentionally avoids implementation placeholders; any template fields are part of user-facing experiment or completion records.
- Type consistency: harness functions are consistently named `load_cases`, `run_cases`, and `write_markdown_report` across implementation and tests.
- Scope check: this plan stops at Stage 0 and does not implement Codex Skill comparisons, MCP, RAG, Agents SDK workflows, deployment, or multi-model routing.
