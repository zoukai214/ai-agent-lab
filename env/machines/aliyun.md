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
