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
