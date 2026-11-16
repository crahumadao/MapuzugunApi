# Deploying Ahumada on PythonAnywhere

Production: https://crahumadao.pythonanywhere.com/
Repository: https://github.com/crahumadao/MapuzugunApi
Production checkout: `/home/crahumadao/MapuzugunApi`
PythonAnywhere WSGI path: `/var/www/crahumadao_pythonanywhere_com_wsgi.py`

## Before deploying

1. Merge a reviewed PR into `main` **only after the CI checks pass**.
2. On PythonAnywhere, inspect **Web > Virtualenv** and confirm it points to the intended environment.
3. Open a PythonAnywhere Bash console and inspect the current checkout:

```bash
cd ~/MapuzugunApi
git status --short
git rev-parse --short HEAD
git fetch origin main
git log --oneline HEAD..origin/main
```

Do not run `git reset --hard` or `git clean -fd`. In particular, do not remove `venv/` or unrelated untracked files.

## Update and validate

Run on **PythonAnywhere**, not on your local workstation:

```bash
cd ~/MapuzugunApi
git pull --ff-only origin main
python scripts/smoke_test.py
```

The smoke test checks the root endpoint and known segmentation of `amun`, `kimvn` and `amuy`. It is not a linguistic benchmark.

If the smoke test fails, **do not reload**. Investigate the traceback and the changes before proceeding.

## WSGI configuration

PythonAnywhere loads the WSGI file configured under **Web > Code**. That file is outside this Git repository, and a `git pull` will **not** update it.

The reference configuration is in `deploy/pythonanywhere_wsgi.py.example`. The active file should expose a module-level Flask object named `application` and ensure the project is on `sys.path`.

Before editing the live WSGI file, inspect it and create a timestamped backup:

```bash
WSGI=/var/www/crahumadao_pythonanywhere_com_wsgi.py
cat "$WSGI"
cp -p "$WSGI" "$WSGI.backup-$(date +%Y%m%d-%H%M%S)"
```

Never overwrite environment-specific settings or credentials without checking them. The reference uses `os.chdir(PROJECT_DIR)` because the current `application.py` loads JSON configuration via relative paths.

## Reload and verify publicly

1. In PythonAnywhere, go to **Web > Reload**.
2. From your workstation, verify the public service:

```bash
curl -fsS --max-time 15 https://crahumadao.pythonanywhere.com/
curl -fsS --max-time 20 -X POST \
  https://crahumadao.pythonanywhere.com/api/wvzalkafe/ \
  -H 'Content-Type: application/json' \
  -d '{"hemvl":"kimvn"}'
```

Expected: HTTP 200 and `code: 1` with two analyses of `kimvn`. Check the response JSON; `curl -f` alone does not validate morphology.

## Troubleshooting

- **HTTP 500 on all routes**: inspect PythonAnywhere **Web > Error log** or, from the PythonAnywhere console, `tail -n 80 /var/log/crahumadao.pythonanywhere.com.error.log`.
- **`AttributeError: ... wsgi has no attribute 'application'`**: check that the active WSGI file is not empty and imports `application` from `application.py`.
- **`FileNotFoundError: config/...`**: verify the working directory is the project root.
- **`ModuleNotFoundError`**: check the PythonAnywhere virtualenv and installed dependencies.
- **Local tests pass but public requests fail**: inspect the WSGI configuration and web logs; the test client does not test the deployed web process.

## Rollback

Record the previously working commit before every update:

```bash
cd ~/MapuzugunApi
git rev-parse HEAD
```

Prefer reverting the offending changes through a reviewed GitHub PR and deploying the resulting `main` commit. If an immediate rollback is required, first preserve local changes and use a temporary checked-out worktree at the known-good commit; update the WSGI project path to that worktree, reload, and verify the public endpoint. Restore the normal path after the fix is merged. Do not hard-reset the production checkout or delete its virtualenv.

If a WSGI edit caused the outage, restore the timestamped WSGI backup instead and reload.
