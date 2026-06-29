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
