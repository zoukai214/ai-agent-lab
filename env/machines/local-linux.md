# Machine: local-linux

## Purpose

Daily learning, note writing, small experiments, and repository maintenance.

## Checks

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```

## Notes

- Record OS version with `lsb_release -a` or `cat /etc/os-release`.
- Record Python version with `python3 --version`.
- Record Git version with `git --version`.
