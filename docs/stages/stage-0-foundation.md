# Stage 0: Foundation

## 目标

建立一个最小基础仓库，使它可以在本地 Linux、GPU 服务器和阿里云上克隆、检查和继续扩展。

## 必需产出

- 用于 docs、环境模板、配置、脚本、harness、实验和知识库的仓库目录。
- 环境检查脚本。
- 最小 harness case 和 runner。
- 实验模板。
- harness runner 和环境检查脚本的测试。

## 验收检查

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
python3 harness/runners/run_echo.py \
  --cases harness/cases/minimal_echo.jsonl \
  --report harness/reports/minimal_echo_report.md
```

Stage 0 通过的含义是：这些命令至少能在一台 Linux 机器上运行成功，并且机器说明记录了迁移到下一台机器时需要检查的内容。

## 完成记录

实施后记录：

```text
Date: 2026-06-29
Commit: 26c9709
Machine: zoukai-Default-string
Environment check: PASS - bash scripts/check/check_environment.sh
Unit tests: PASS - python3 -m unittest discover -s tests -v, 4 tests
Minimal harness: PASS - cases=2 failed=0
Notes: Secret scan and unfinished-marker scan returned no matches.
```
