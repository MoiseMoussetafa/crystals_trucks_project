# Fichier python pour Tests unitaires Git

from src.trucks.main import generate_map

def inc(x):
    return x + 1

def test_collaboratif():
    assert inc(15) == 16

def test2():
    generate_map("filename") == 0
