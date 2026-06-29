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
