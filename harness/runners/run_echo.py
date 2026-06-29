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
