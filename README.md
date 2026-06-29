# ai-agent-lab

个人 AI 工程实验室，用来深入学习 Codex、构建 AI Agent、管理知识系统、评估工作流，并把同一套环境迁移到本地 Linux、GPU 服务器和阿里云。

## 当前阶段

Stage 0 用来打基础：

- 建立学习笔记、实验、harness、配置和知识库的仓库结构。
- 提供 Linux 机器上的最小环境检查。
- 提供一个可复现的最小 harness，可以运行测试用例并生成报告。
- 提供后续阶段实验记录和费曼式复盘模板。

## 快速开始

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
python3 harness/runners/run_echo.py \
  --cases harness/cases/minimal_echo.jsonl \
  --report harness/reports/minimal_echo_report.md
```

## 仓库地图

- `docs/`：路线图、阶段说明、学习笔记、参考资料、复盘，以及 Superpowers 规格和计划。
- `env/`：环境变量模板和不同机器的迁移记录。
- `configs/`：Codex、MCP、Agent 和模型配置示例。
- `scripts/`：安装、同步、检查和运行脚本。
- `harness/`：可复用的评估用例、runner、指标和报告。
- `experiments/`：小实验和对比实验。
- `projects/`：阶段项目，后续可以拆成独立系统。
- `knowledge/`：个人知识库的 inbox、processed notes 和 indexes。
- `tests/`：脚本、harness 和项目测试。

## 规则

- 不要把 secrets、tokens、private keys、model weights 或大型数据集提交到 Git。
- 每个实验都要记录输入、运行命令、输出和简短结论。
- 每个新功能都要有聚焦的测试。
- 在阶段确实需要重型工具之前，优先使用可移植的 Python 3 和 shell 脚本。
