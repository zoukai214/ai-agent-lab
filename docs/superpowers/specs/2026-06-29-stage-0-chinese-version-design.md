# Stage 0 中文主版本设计

## 背景

当前 Stage 0 基础结构已经完成，但主要入口文档、路线图、机器说明、实验模板和知识库说明以英文为主。这个仓库是个人 AI Agent 工程学习仓库，学习和复盘效率优先于对外英文展示，因此需要一个中文主版本分支。

## 目标

在 `stage-0-chinese-version` 分支上，将 Stage 0 相关说明改为中文为主，保留必要英文术语、命令、路径和工具名，让仓库可以直接作为中文学习入口使用。

## 修改范围

中文化以下文档：

- `README.md`
- `AGENTS.md`
- `docs/roadmap/README.md`
- `docs/stages/stage-0-foundation.md`
- `env/machines/local-linux.md`
- `env/machines/gpu-server.md`
- `env/machines/aliyun.md`
- `configs/codex/README.md`
- `experiments/000-template/README.md`
- `knowledge/inbox/README.md`
- `knowledge/processed/README.md`
- `knowledge/index/README.md`
- `harness/reports/README.md`

不修改以下文件：

- `scripts/check/check_environment.sh`
- `harness/runners/run_echo.py`
- `tests/**`
- `env/templates/env.example`
- `harness/cases/minimal_echo.jsonl`
- `harness/reports/minimal_echo_report.md`

这些文件属于可执行行为、测试、配置样例或生成报告。中文化分支的第一步只调整人工阅读文档，不改变 Stage 0 的运行行为。

## 文档风格

- 中文为主，句子简洁，面向个人学习和复盘。
- 保留 `Codex`、`MCP`、`RAG`、`AI Agent`、`harness`、`Stage` 等常用技术词。
- 保留所有命令、路径、目录名和文件名的英文原文。
- 不引入大型教程；每个文件只说明当前目录或当前阶段需要知道的内容。
- 不添加空泛的未完成标记。

## 验证方式

改动完成后运行：

```bash
python3 -m unittest discover -s tests -v
bash scripts/check/check_environment.sh
python3 harness/runners/run_echo.py \
  --cases harness/cases/minimal_echo.jsonl \
  --report harness/reports/minimal_echo_report.md
rg -n "TB[D]|TO[D]O|待[定]|占[位]" README.md AGENTS.md docs env configs harness experiments knowledge
```

预期结果：

- 单元测试全部通过。
- 环境检查脚本退出码为 0。
- 最小 harness 输出 `cases=2 failed=0`。
- 未完成标记扫描无匹配。

## 非目标

- 不重写代码、测试或 shell 脚本。
- 不新增 Stage 1 内容。
- 不翻译历史 Superpowers 计划和规格文档，除非它们会影响当前中文学习入口。
- 不调整仓库结构。

## 风险与处理

- 风险：中文化时不小心改变命令或路径。
  - 处理：命令块和路径保持原样，并通过验证命令确认行为未变。
- 风险：中英文混排导致文档风格不统一。
  - 处理：正文中文化，技术名词保留英文，避免逐词翻译。
- 风险：把模板字段误判成未完成内容。
  - 处理：实验模板使用明确的中文字段说明，避免使用会被扫描命中的未完成标记。
