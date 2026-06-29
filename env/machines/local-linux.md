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
