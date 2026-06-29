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
