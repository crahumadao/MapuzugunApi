"""Prueba de humo de la construcción del árbol morfológico."""

from kvzawpeyvm.wvzalkawe.koyam import Koyam


def test_koyam_finds_candidates_for_known_word():
    tree = Koyam("kimvn")
    tree.zewmakoyamvn()

    assert tree.kom_row
    assert any(branch.xoys for branch in tree.kom_row)
