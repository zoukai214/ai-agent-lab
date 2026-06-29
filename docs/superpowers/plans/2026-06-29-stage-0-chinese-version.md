# Stage 0 Chinese Version Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the Stage 0 learning entry documents to a Chinese-first version on the `stage-0-chinese-version` branch without changing executable behavior.

**Architecture:** Keep the existing repository structure unchanged. Translate only human-facing Stage 0 documents, preserve paths, commands, file names, and common technical terms such as Codex, MCP, RAG, AI Agent, Stage, and harness. Validate that tests and harness behavior remain unchanged after documentation edits.

**Tech Stack:** Markdown, Git, Python 3 standard library, Bash, ripgrep.

---

## File Structure

- Modify: `README.md` as the Chinese-first repository entry point.
- Modify: `AGENTS.md` as the Chinese-first repo-local agent rules file.
- Modify: `docs/roadmap/README.md` as the Chinese learning roadmap.
- Modify: `docs/stages/stage-0-foundation.md` as the Chinese Stage 0 acceptance document.
- Modify: `env/machines/local-linux.md`, `env/machines/gpu-server.md`, `env/machines/aliyun.md` as Chinese machine notes.
- Modify: `configs/codex/README.md` as Chinese Codex configuration notes.
- Modify: `experiments/000-template/README.md` as the Chinese experiment template.
- Modify: `knowledge/inbox/README.md`, `knowledge/processed/README.md`, `knowledge/index/README.md` as Chinese knowledge workflow notes.
- Modify: `harness/reports/README.md` as Chinese report storage rules.
- Do not modify: `scripts/check/check_environment.sh`, `harness/runners/run_echo.py`, `tests/**`, `env/templates/env.example`, `harness/cases/minimal_echo.jsonl`, `harness/reports/minimal_echo_report.md`.

## Task 1: Chinese Repository Entry Points

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`

- [ ] **Step 1: Replace `README.md` with Chinese-first content**

````markdown
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
````

- [ ] **Step 2: Replace `AGENTS.md` with Chinese-first content**

````markdown
# ai-agent-lab Agent 规则

## 项目用途

这个仓库是个人 AI Agent 工程实验室。它保存学习计划、笔记、实验、harness、配置和阶段项目，用来系统学习并实践 AI Agent 工程。

## 工作规则

- 需要注释时，代码注释使用中文。
- 不要提交 secrets、tokens、private keys、model weights 或大型数据集。
- 不要修改 `CMakeLists.txt` 等构建选项，除非用户明确要求。
- 新增可执行行为时，必须有聚焦的测试。
- Stage 0 基础设施优先使用 Python 3 标准库和 Bash。
- 学习笔记放在 `docs/`，实验放在 `experiments/`，可复用评估代码放在 `harness/`，阶段项目放在 `projects/`。

## 验证

在认为改动完成之前，运行：

```bash
python3 -m unittest discover -s tests
```

如果改动涉及环境相关内容，也运行：

```bash
bash scripts/check/check_environment.sh
```
````

- [ ] **Step 3: Inspect the rendered entry files**

Run:

```bash
sed -n '1,220p' README.md
sed -n '1,220p' AGENTS.md
```

Expected: both files are Chinese-first, preserve commands and paths, and contain no unfinished markers.

- [ ] **Step 4: Commit**

```bash
git add README.md AGENTS.md
git commit -m "docs: localize repository entry points"
```

## Task 2: Chinese Learning and Stage Documents

**Files:**
- Modify: `docs/roadmap/README.md`
- Modify: `docs/stages/stage-0-foundation.md`

- [ ] **Step 1: Replace `docs/roadmap/README.md`**

```markdown
# AI Agent 学习路线图

这份路线图记录从 Codex 深度用户成长为 AI Agent 工程师的六个月路径。

## 阶段

| Stage | 主题 | 主要产出 |
| --- | --- | --- |
| 0 | Foundation | 可迁移仓库结构、环境检查、最小 harness |
| 1 | Codex Deep Usage | Codex 工作流模板，以及 AGENTS 和 Skill 对比 |
| 2 | Agent Principles | 可解释的最小 Agent，以及 context/memory 实验 |
| 3 | MCP and Knowledge | 可搜索的个人知识库原型 |
| 4 | Agent Engineering | 可追踪、有观测能力的 workflow agent |
| 5 | Advanced Systems | 自托管个人 AI Agent 平台原型 |

## 学习规则

每个阶段都必须产出一个小测试、一个小项目或可复用资产、一份费曼式解释，以及一个对比结论。
```

- [ ] **Step 2: Replace `docs/stages/stage-0-foundation.md`**

````markdown
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
````

- [ ] **Step 3: Inspect the rendered stage docs**

Run:

```bash
sed -n '1,180p' docs/roadmap/README.md
sed -n '1,220p' docs/stages/stage-0-foundation.md
```

Expected: both files are Chinese-first and preserve the Stage table, commands, and completion evidence.

- [ ] **Step 4: Commit**

```bash
git add docs/roadmap/README.md docs/stages/stage-0-foundation.md
git commit -m "docs: localize stage 0 learning docs"
```

## Task 3: Chinese Environment and Codex Notes

**Files:**
- Modify: `env/machines/local-linux.md`
- Modify: `env/machines/gpu-server.md`
- Modify: `env/machines/aliyun.md`
- Modify: `configs/codex/README.md`

- [ ] **Step 1: Replace `env/machines/local-linux.md`**

````markdown
# Machine: local-linux

## 用途

日常学习、写笔记、小实验和仓库维护。

## 检查命令

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```

## 记录事项

- 用 `lsb_release -a` 或 `cat /etc/os-release` 记录 OS 版本。
- 用 `python3 --version` 记录 Python 版本。
- 用 `git --version` 记录 Git 版本。
````

- [ ] **Step 2: Replace `env/machines/gpu-server.md`**

````markdown
# Machine: gpu-server

## 用途

GPU 实验、本地模型试验和长时间运行的 Agent 工作流。

## 检查命令

```bash
bash scripts/check/check_environment.sh
nvidia-smi
python3 -m unittest discover -s tests
```

## 记录事项

- 从 `nvidia-smi` 记录 GPU 型号和 driver 版本。
- model weights 和 datasets 必须放在 Git 之外。
- 任何本地路径差异都记录在未跟踪的 `.env` 文件中。
````

- [ ] **Step 3: Replace `env/machines/aliyun.md`**

````markdown
# Machine: aliyun

## 用途

云端迁移检查、部署实验和网络对比测试。

## 检查命令

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```

## 记录事项

- 记录实例规格、region、OS image、disk size 和网络限制。
- 云账号凭据必须放在 Git 之外。
- 改脚本之前，先和 `local-linux` 的命令输出做对比。
````

- [ ] **Step 4: Replace `configs/codex/README.md`**

````markdown
# Codex 配置说明

这个目录保存本仓库使用 Codex 的示例和约定。

## 边界

- 仓库级 Agent 规则放在根目录 `AGENTS.md`。
- 可复用工作流只有在多次重复并验证后，才整理成 Skill。
- prompt 实验放在 `experiments/stage-1/`。
- secrets 和个人账号配置不属于这个仓库。

## Stage 0 验证

使用 Codex 运行一次仓库检查，然后和手动命令输出做对比：

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```
````

- [ ] **Step 5: Inspect environment and Codex docs**

Run:

```bash
sed -n '1,180p' env/machines/local-linux.md
sed -n '1,180p' env/machines/gpu-server.md
sed -n '1,180p' env/machines/aliyun.md
sed -n '1,180p' configs/codex/README.md
```

Expected: files are Chinese-first and keep command blocks unchanged.

- [ ] **Step 6: Commit**

```bash
git add env/machines/local-linux.md env/machines/gpu-server.md env/machines/aliyun.md configs/codex/README.md
git commit -m "docs: localize environment and codex notes"
```

## Task 4: Chinese Experiment, Knowledge, and Report Notes

**Files:**
- Modify: `experiments/000-template/README.md`
- Modify: `knowledge/inbox/README.md`
- Modify: `knowledge/processed/README.md`
- Modify: `knowledge/index/README.md`
- Modify: `harness/reports/README.md`

- [ ] **Step 1: Replace `experiments/000-template/README.md`**

```markdown
# 实验模板

开始新实验时，复制这个目录。

## 问题

写清楚本次实验要验证的具体问题。

## 设置

- 机器：
- 日期：
- 提交：
- 输入：
- 命令：

## 结果

记录观察到的输出、报告路径、延迟、可获得的成本信息，以及失败说明。

## 结论

总结发生了什么变化、什么没有变化，以及结果是否可复现。
```

- [ ] **Step 2: Replace `knowledge/inbox/README.md`**

```markdown
# Knowledge Inbox

这里保存尚未处理的原始链接、笔记和来源引用。

不要把私人文档、secrets、大型 PDF 或授权受限的数据集提交到 Git。
```

- [ ] **Step 3: Replace `knowledge/processed/README.md`**

```markdown
# Processed Knowledge

这里保存清理后的笔记、摘要和费曼式解释。

每条 processed note 都应该链接回来源，并包含一段用自己语言写的简短结论。
```

- [ ] **Step 4: Replace `knowledge/index/README.md`**

```markdown
# Knowledge Index

这里保存索引、标签、来源映射和检索说明。

这个 index 应该帮助未来的 Codex、MCP 或 RAG 工作流快速找到合适材料。
```

- [ ] **Step 5: Replace `harness/reports/README.md`**

```markdown
# Harness Reports

这里可以保存 harness 运行生成的小型报告，前提是这些报告对学习记录有价值。

不要提交大型日志、私人数据、包含 secrets 的模型输出，或成本很高的原始 trace。
```

- [ ] **Step 6: Inspect experiment, knowledge, and report docs**

Run:

```bash
sed -n '1,160p' experiments/000-template/README.md
sed -n '1,120p' knowledge/inbox/README.md
sed -n '1,120p' knowledge/processed/README.md
sed -n '1,120p' knowledge/index/README.md
sed -n '1,120p' harness/reports/README.md
```

Expected: files are Chinese-first, concise, and contain no unfinished markers.

- [ ] **Step 7: Commit**

```bash
git add experiments/000-template/README.md knowledge/inbox/README.md knowledge/processed/README.md knowledge/index/README.md harness/reports/README.md
git commit -m "docs: localize experiment and knowledge notes"
```

## Task 5: Full Validation

**Files:**
- Modify: no source files expected unless validation exposes a defect.

- [ ] **Step 1: Run all tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: 4 tests pass.

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

- [ ] **Step 4: Check unfinished markers**

Run:

```bash
rg -n "TB[D]|TO[D]O|待[定]|占[位]" README.md AGENTS.md docs env configs harness experiments knowledge
```

Expected: exit code 1 with no matches.

- [ ] **Step 5: Check branch state**

Run:

```bash
git status --short --branch
```

Expected: branch is `stage-0-chinese-version`; no uncommitted source changes remain.

## Self-Review

- Spec coverage: Tasks cover every file listed in the approved design and exclude code, tests, config samples, case files, and generated reports as required.
- Scope check: The plan only localizes Stage 0 reading documents and does not add Stage 1 content or change repository structure.
- Validation check: The plan verifies tests, environment check, minimal harness, unfinished-marker scan, and branch state.
