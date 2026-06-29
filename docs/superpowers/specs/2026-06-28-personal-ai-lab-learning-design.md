# Personal AI Lab 学习与实践设计

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为具备算法工程背景、已使用 Codex CLI 一段时间的学习者，设计一条从 Codex 深度使用出发、逐步成长为 AI Agent 工程师的 6 个月学习与实践路线，并能在本地 Linux、3060 服务器与阿里云之间迁移和同步。

**Architecture:** 采用“前置学习底座 + Codex 工程化使用 + Agent 原理 + Agent 工程 + 高级扩展”五层结构。`harness` 作为全程统一评测底座，GitHub 作为唯一事实源，所有学习材料、实验记录、配置模板和对比结果都必须可追溯、可复现、可迁移。

**Tech Stack:** Codex CLI, AGENTS.md, Skills, MCP, OpenAI Agents SDK, RAG / Knowledge Base, harness/eval, Docker, Linux, GitHub, Markdown, PDF.

---

## 1. 背景与目标

本计划面向以下现状：
- 已经使用过 Codex CLI，理解基本交互。
- 已经创建过自己的 Skill，但对更系统的 Agent 工程体系仍在进阶阶段。
- 对 MCP、知识库、harness、多模型、多模态、压缩、记忆等概念希望系统补齐。
- 学习环境需要在本地 Linux、3060 Linux 服务器和阿里云之间迁移与同步。
- 学习文档、笔记、实验记录与结果需要同步到 GitHub。
- 所有学习目标与测试尽量用费曼学习法验收。

最终目标不是“会用 Codex”，而是能够独立设计、实现、部署和评估一个自托管 AI Agent 系统。

## 2. 设计原则

- 从工程问题出发，不从纯概念出发。
- `harness` 先行，评测底座贯穿全程。
- Codex 是入口，不是终点。
- 每一阶段都必须有 `小测试 + 小工程 + 费曼讲解 + 对比结论`。
- 每个工具、框架或技能都必须回答三个问题：为什么用、什么时候用、如何验收。
- 所有学习资料与产物都必须 GitHub 化，避免只停留在聊天记录里。

## 3. 仓库目录设计

仓库采用“单仓库 + 子文件夹分层”的方式组织。`ai-agent-lab` 是唯一事实源，学习资料、实验、配置模板、评测结果和阶段性小工程都先放在同一个 Git 仓库中。只有当某个阶段工程成熟到需要单独发布、部署或开源时，才考虑从 `projects/<name>` 拆成独立仓库。

目录组织采用“工程资产类型为主，阶段索引为辅”的混合结构：

```text
ai-agent-lab/
  README.md
  AGENTS.md

  docs/
    roadmap/
    stages/
    notes/
    references/
    reviews/
    superpowers/

  env/
    templates/
    machines/
    bootstrap/

  configs/
    codex/
    mcp/
    agents/
    models/

  scripts/
    setup/
    sync/
    check/
    run/

  harness/
    cases/
    runners/
    metrics/
    reports/

  experiments/
    000-template/
    stage-0/
    stage-1/
    stage-2/
    stage-3/
    stage-4/
    stage-5/

  projects/
    stage-1-codex-workflow/
    stage-2-minimal-agent/
    stage-3-knowledge-base/
    stage-4-traceable-agent/
    stage-5-self-hosted-agent-platform/

  knowledge/
    inbox/
    processed/
    index/
    datasets/

  tests/
    harness/
    scripts/
    projects/
```

一级目录职责：

- `docs/`：学习路线、阶段说明、日常笔记、资料索引、阶段复盘和 Superpowers 设计/计划文档。
- `env/`：本地 Linux、3060 服务器、阿里云环境差异、环境变量模板和初始化说明。
- `configs/`：Codex、MCP、Agents SDK、多模型路由等工具配置模板。
- `scripts/`：环境初始化、同步、检查和实验启动脚本。
- `harness/`：全程共用评测底座，保存测试用例、执行器、指标定义和报告。
- `experiments/`：小测试和对比实验，按阶段归档。
- `projects/`：阶段性小工程，避免把工程代码混进学习笔记。
- `knowledge/`：个人知识库原型，采用 `inbox -> processed -> index` 的整理链路。
- `tests/`：harness、脚本和阶段工程的测试入口。

目录落地规则：

- `docs/stages/` 回答“当前阶段学什么、验收什么、如何复盘”。
- `experiments/` 中每个实验必须包含输入、运行方式、结果记录和对比结论。
- `projects/` 中每个小工程必须能独立说明目标、运行方式和测试方式。
- `harness/` 不放入某一个阶段目录，保持跨阶段复用。
- `env/` 记录机器与运行环境差异，`configs/` 记录工具和 agent 配置。
- 大文件、模型权重、私钥、真实 token、云服务器敏感配置不进入仓库，只保留模板和说明。

阶段 0 的最小落地范围：

```text
docs/roadmap/
docs/stages/
env/templates/
env/machines/
configs/codex/
scripts/check/
harness/cases/
harness/runners/
harness/reports/
experiments/000-template/
knowledge/inbox/
knowledge/processed/
knowledge/index/
```

## 4. 学习分层

### 4.1 前置层：环境与评测底座

目标是先把“可迁移、可复现、可验证”的学习基础搭起来。

包含内容：
- 统一仓库结构。
- 本地 Linux / 3060 / 阿里云一致的启动方式。
- 环境变量模板、启动脚本、依赖记录。
- `harness` 与对比实验模板。
- 学习笔记与实验记录规范。

建议产出：
- `README.md`：一键进入学习环境的说明。
- `docs/`：学习笔记、实验记录、阶段总结。
- `scripts/`：统一启动、同步、校验脚本。
- `experiments/`：每次对比测试独立目录。

验收标准：
- 同一套仓库能在至少两种 Linux 环境启动。
- 同一个实验可以重复运行并得到可比较结果。
- 能明确记录“环境差异导致的结果差异”。

### 4.2 Codex 工程层：深度使用但不强依赖底层原理

这一层重点是把 Codex 用成工程协作工具，而不是只会聊天。

学习内容：
- `AGENTS.md` 的分层约束与任务边界。
- Skill 的拆分、复用和工作流化。
- 任务分解、代码修改、文档生成、代码审查。
- subagent / 角色化工作流。
- 与仓库规范结合的提示词约束。

推荐使用的工具或框架：
- `superpower` 风格的 Skill 设计。
- 自定义 `AGENTS.md` 规则。
- 轻量脚本化任务模板。

验收标准：
- 能解释一个任务为什么适合写成 Skill。
- 能解释一个规则为什么适合放在 AGENTS.md 而不是 prompt 里。
- 同一个任务能分别用“裸提示词 / Skill / AGENTS 约束”完成并比较质量。

### 4.3 Agent 原理层：补齐深度使用所需的底层知识

这一层补齐你提到的 `记忆、压缩、多步推理、规划` 等能力。

学习内容：
- context window 与上下文管理。
- short-term memory / long-term memory。
- compression / summarization。
- tool use / action loop。
- planning / reflection / retry。
- 单轮回答与多步 agent 的边界。

验收标准：
- 能说明为什么上下文会膨胀。
- 能说明压缩和记忆的区别。
- 能解释一个任务失败是模型、工具还是状态设计的问题。

### 4.4 Agent 工程层：MCP、知识库、RAG、工作流

这一层开始进入可落地的工程体系。

学习内容：
- MCP host / client / server。
- tools / resources / prompts 的划分。
- 文件系统知识库。
- Markdown / PDF / Git 资料检索。
- RAG 与知识库接入。
- 工作流编排与多步执行。

推荐使用的工具或框架：
- Filesystem MCP。
- 个人知识库目录。
- OpenAI Agents SDK。
- 轻量 RAG 实验框架。

验收标准：
- 能把一个问题从“直接问模型”切换到“检索后回答”。
- 能清楚解释 MCP 为什么不是简单插件系统。
- 能把自己的知识库接入 Codex 或 agent 工作流。

### 4.5 高级扩展层：多模型、多模态、多 Agent、自托管部署

这一层放在后面，不前置。

学习内容：
- 多模型路由与切换策略。
- 多模态输入输出。
- multi-agent 协作。
- 自托管部署。
- 可观测性、稳定性、成本控制。

验收标准：
- 能说明引入多模型的收益和代价。
- 能说明多模态解决了什么单模态做不到的问题。
- 能在本地与阿里云上迁移同一套系统。

## 5. 工具与框架插入原则

工具和框架不单独堆砌，必须嵌入阶段目标。

- `harness`：前置并贯穿全程，用于验证学习效果和对比实验。
- `superpower skill`：放在 Codex 工程层，作为工作流复用的样板。
- `MCP`：放在 Agent 工程层，作为工具生态和资源接入方式。
- `OpenAI Agents SDK`：放在 Agent 工程层，用于从概念过渡到可运行 agent。
- `多模型 / 多模态`：放在高级扩展层，作为工程增强项。

每个工具都必须完成以下验收：
- 是否能显著提升可复用性。
- 是否降低任务复杂度。
- 是否能在本地和云环境一致运行。
- 是否能被 `harness` 测出来。

## 6. 官方文档映射

每个阶段必须指定要看的官方资料模块。

### 6.1 Codex 相关

建议优先学习：
- Codex CLI
- AGENTS.md
- Skills
- Best practices
- Subagents
- Codex with Agents SDK

对应学习目标：
- 搞清 Codex 的工作方式。
- 搞清规则、Skill 和子代理的边界。
- 学会把工程约束沉淀成可复用规则。

### 6.2 Agents SDK 相关

建议优先学习：
- Quickstart
- Define agents
- Running agents
- Orchestration and handoffs
- Tracing / observability
- Sandboxes

对应学习目标：
- 搞清 agent 的定义、执行和编排。
- 搞清工具调用、handoff、追踪与调试。
- 搞清 agent 为什么会失败，如何观测。

### 6.3 文档阅读方式

每次学习只读“本阶段需要的模块”，不做整站通读。
每个模块都必须输出：
- 一段自己的解释。
- 一个小实验。
- 一条可复现的结论。

## 7. 阶段性学习路线

### 阶段 0：学习底座

产出：
- 统一目录结构。
- 环境同步脚本。
- `harness` 骨架。
- 实验记录模板。

测试：
- 本地 Linux 与阿里云都能跑同一个最小实验。
- 同一输入在不同环境下的结果可记录、可比较。

### 阶段 1：Codex 深度使用

重点：
- AGENTS.md。
- Skill 工程化。
- 工程任务拆分。
- 小型协作流。

小测试：
- 同一任务分别用裸提示词、Skill、AGENTS 约束执行。

小工程：
- 个人 Codex 学习工作流模板仓库。

### 阶段 2：Agent 原理补齐

重点：
- context 管理。
- memory。
- compression。
- planning。

小测试：
- 同一任务对比“单轮回答”和“多步 agent”。

小工程：
- 一个最小可解释 agent。

### 阶段 3：MCP 与知识系统

重点：
- Filesystem MCP。
- 个人知识库。
- RAG。

小测试：
- 直接问模型 vs 检索后回答。

小工程：
- 可检索的个人知识库原型。

### 阶段 4：Agent 工程与编排

重点：
- OpenAI Agents SDK。
- 工作流编排。
- tracing。

小测试：
- 单 agent vs 多步 workflow。

小工程：
- 可追踪的任务执行 agent。

### 阶段 5：高级扩展

重点：
- 多模型。
- 多模态。
- multi-agent。
- 部署。

小测试：
- 本地 vs 阿里云部署对比。

小工程：
- 自托管个人 AI Agent 平台原型。

## 8. 费曼式验收

每个阶段固定输出：
- 一页总结。
- 一个可运行实验。
- 一次口头讲解或文字复盘。

每个主题再补一个对比表：
- 本地 Linux vs 阿里云。
- 裸提示词 vs Skill。
- 直接调用模型 vs 检索增强。
- 单步任务 vs 多步 agent。

## 9. 质量门槛

以下情况视为未通过：
- 只有概念没有实验。
- 只有实验没有对比。
- 只有结论没有复现路径。
- 工具引入了但没有验收标准。
- 环境能跑但不能迁移。

## 10. 结论

本计划不把 Codex 当终点，而是把 Codex 当入口，把 `harness + 工程化工作流 + Agent 原理 + MCP + 知识库 + 部署` 作为完整成长路径。学习节奏应当始终围绕“可验证、可迁移、可复用”展开。
