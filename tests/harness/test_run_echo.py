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
