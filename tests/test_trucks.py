import src.trucks as trucks
import pathlib

THIS_DIR = pathlib.Path(__file__).parent.__str__()
MAP_FILE = THIS_DIR + "/map.txt"


def test_create_game_seed_0():
    seed = 0
    filename = MAP_FILE

    ref_nb_camions = 2
    ref_grid = [[0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 2, 1, 0, 0, 1, 2],
                [0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 2, 1, 0, 2, 1, 1, 0, 2, 0, 2, 1, 0, 2],
                [0, 2, 2, 2, 2, 0, 1, 0, 0, 2, 0, 0, 2, 2, 0, 0],
                [1, 2, 0, 2, 0, 2, 1, 1, 0, 2, 0, 1, 1, 2, 0, 0],
                [0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0],
                [2, 2, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 2, 2, 1, 0, 2, 0, 0, 2, 2, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 0],
                [2, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 2, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1, 0, 2, 0, 0, 0],
                [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0]]
    ref_width = 16
    ref_height = 15

    assert trucks.create_game(seed, filename) == (
        ref_nb_camions, ref_grid, ref_width, ref_height
    )


def test_create_game_seed_5():
    seed = 5
    filename = MAP_FILE

    ref_nb_camions = 3
    ref_grid = [[2, 1, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 1, 0, 2],
                [0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 1, 0, 2, 1, 2],
                [0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                [2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 1, 1, 2, 2, 0, 0, 0],
                [0, 1, 1, 2, 0, 0, 0, 1, 0, 2, 2, 0, 1, 0, 1, 2, 2],
                [1, 1, 0, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 1, 0],
                [1, 1, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0],
                [0, 0, 0, 2, 0, 1, 1, 0, 0, 1, 0, 0, 1, 2, 2, 0, 0]]
    ref_width = 17
    ref_height = 10

    assert trucks.create_game(seed, filename) == (
        ref_nb_camions, ref_grid, ref_width, ref_height
    )


def test_truck_creation_0_0_0():
    camion = trucks.Camion(0, 0, 0)

    assert (camion._id, camion.x, camion.y) == (0, 0, 0)


def test_truck_creation_5_20_3():
    camion = trucks.Camion(5, 20, 3)

    assert (camion._id, camion.x, camion.y) == (5, 20, 3)


def test_truck_dig_0_0(capsys):
    camion_test = trucks.Camion(0, 0, 0)
    trucks.NB_TOUR = 0
    camion_test.dig()

    captured = capsys.readouterr()
    assert captured.out == "0 DIG 0 0 0\n"


def test_truck_dig_25_4(capsys):
    camion_test = trucks.Camion(3, 25, 4)
    trucks.NB_TOUR = 72
    camion_test.dig()

    capture = capsys.readouterr()
    assert capture.out == "72 DIG 3 25 4\n"


def test_truck_progress_dig_2(capsys):
    camion = trucks.Camion(0, 0, 0)
    camion.set_target(0, 0)
    trucks.NB_TOUR = 0
    trucks.GRID = [[2]]

    camion.progress()
    capture = capsys.readouterr()
    assert capture.out == "0 DIG 0 0 0\n"
    trucks.NB_TOUR += 1
    camion.progress()
    capture = capsys.readouterr()
    assert capture.out == "1 DIG 0 0 0\n"
