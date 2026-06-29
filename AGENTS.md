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
