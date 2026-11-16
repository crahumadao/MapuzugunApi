"""Run local Flask smoke checks without starting a web server.

Usage: python scripts/smoke_test.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from application import application  # noqa: E402


def main():
    client = application.test_client()

    response = client.get("/")
    assert response.status_code == 200, response.status_code
    assert "Mari mari" in json.loads(response.get_data(as_text=True))

    expected = {
        "amun": {("amu", "n")},
        "kimvn": {("kim", "vn"), ("kimvn",)},
        "amuy": {("amu", "y")},
    }

    for word, segments in expected.items():
        response = client.post("/api/wvzalkafe/", json={"hemvl": word})
        assert response.status_code == 200, (word, response.status_code)
        payload = json.loads(response.get_data(as_text=True))
        assert payload["code"] == 1, (word, payload)
        assert len(payload["data"]) == 1, (word, payload)
        analyses = payload["data"][0]["hemvlkawe"]
        actual = {tuple(item[3]) for item in analyses}
        assert actual == segments, (word, actual, segments)
        print(f"PASS {word}: {len(actual)} analysis(es)")

    print("LOCAL API SMOKE TEST OK")


if __name__ == "__main__":
    main()
