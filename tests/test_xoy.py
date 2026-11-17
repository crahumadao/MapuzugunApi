"""Regresiones del motor de coincidencia de morfemas."""

import pytest

from kvzawpeyvm.wvzalkawe.xoy import Xoy


@pytest.mark.parametrize(
    ("pattern", "word", "expected"),
    [
        ("kim", "kimvn", ("kim", "vn")),
        ("^amu", "amun", ("amu", "n")),
        ("^kimvn$", "kimvn", ("kimvn", "")),
    ],
)
def test_matching_and_segmentation(pattern, word, expected):
    rule = Xoy(regex=pattern)

    assert rule.mvli(word) is True
    assert rule.wvzage(word) == expected
    assert rule._compiled_regex.pattern == rule.regex


def test_unmatched_rule_returns_none():
    rule = Xoy(regex="^kim")

    assert rule.mvli("amun") is False
    assert rule.wvzage("amun") is None


def test_patterns_are_anchored_to_the_start():
    rule = Xoy(regex="kim")

    assert rule.regex == "^kim"
    assert rule.mvli("akimvn") is False
