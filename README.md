# MapuzugunApi — Ahumada

Flask API for Mapuzugun orthographic conversion and morphological analysis.

## Endpoints

- `GET /` — service greeting.
- `GET /api/narvmal/metadata/` — metadata.
- `POST /api/wvzalkafe/` — morphological analysis, JSON `{"hemvl": "kimvn"}`.
- `POST /api/rulpazugual/` — orthographic conversion.
- `POST /api/chuchiWirintukun/` — orthography identification.

## Development

The existing application uses a legacy Flask/pandas stack. CI targets Python 3.10 with compatibility constraints in `constraints-ci.txt`.

```bash
python -m pip install -c constraints-ci.txt -r requirements.txt -r requirements-ci.txt
python -m pytest -q
python scripts/smoke_test.py
```

Run from the repository root; `application.py` currently loads `config/*.json` using relative paths.

## Deployment

Production runs on PythonAnywhere. See [deployment and rollback guide](docs/deployment-pythonanywhere.md) and [example WSGI file](deploy/pythonanywhere_wsgi.py.example).

**Deployments are manual.** GitHub Actions runs tests; it does not push to PythonAnywhere or reload the web app.

## Test scope

The regression suite covers `Xoy` matching and a few manually verified API responses. It does **not** establish broad linguistic accuracy or coverage. A morphology benchmark requires separate linguistic design and review.
