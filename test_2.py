import game 
from game import init_game

def test_max_values():
    assert game.MAX_NB_TRUCKS == 9
    assert game.MAX_WIDTH == 30
    assert game.MAX_HEIGHT == 20