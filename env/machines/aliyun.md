# Machine: aliyun

## Purpose

Cloud migration checks, deployment experiments, and network comparison tests.

## Checks

```bash
bash scripts/check/check_environment.sh
python3 -m unittest discover -s tests
```

## Notes

- Record instance type, region, OS image, disk size, and network constraints.
- Keep cloud credentials outside Git.
- Compare command outputs with `local-linux` before changing scripts.
