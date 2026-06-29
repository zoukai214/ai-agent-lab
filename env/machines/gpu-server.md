# Machine: gpu-server

## Purpose

GPU-backed experiments, local model trials, and longer-running agent workflows.

## Checks

```bash
bash scripts/check/check_environment.sh
nvidia-smi
python3 -m unittest discover -s tests
```

## Notes

- Record GPU model and driver version from `nvidia-smi`.
- Keep model weights and datasets outside Git.
- Document any local path differences in an untracked `.env` file.
