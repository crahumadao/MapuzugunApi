"""Regresiones de la API pública, basadas en respuestas verificadas en producción."""

import json

import pytest

from application import application


@pytest.fixture(scope="module")
def client():
    application.config["TESTING"] = True
    with application.test_client() as test_client:
        yield test_client


@pytest.mark.parametrize(
    ("word", "expected_segments"),
    [
        ("amun", {("amu", "n")}),
        ("kimvn", {("kim", "vn"), ("kimvn",)}),
        ("amuy", {("amu", "y")}),
    ],
)
def test_analyzer_known_words(client, word, expected_segments):
    response = client.post("/api/wvzalkafe/", json={"hemvl": word})

    assert response.status_code == 200
    payload = json.loads(response.get_data(as_text=True))
    assert payload["code"] == 1
    assert len(payload["data"]) == 1

    word_result = payload["data"][0]
    assert word_result["xipai"] is True

    actual_segments = {
        tuple(analysis[3]) for analysis in word_result["hemvlkawe"]
    }
    assert actual_segments == expected_segments


def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Mari mari" in json.loads(response.get_data(as_text=True))


def test_metadata_endpoint(client):
    response = client.get("/api/narvmal/metadata/")

    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) is not None
