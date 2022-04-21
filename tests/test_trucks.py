# Fichier python pour Tests unitaires Git
import pytest

def inc(x):
    return x + 1

def test_collaboratif():
    assert inc(15) == 16

