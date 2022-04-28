from fileinput import filename
import src.trucks as trucks
import pathlib
import main

THIS_DIR = pathlib.Path(__file__).parent.__str__()
MAP_FILE = THIS_DIR + "/map.txt"


def test_main():
    assert main != None


def test_create_game_seed_0():
    seed = 0
    filename = MAP_FILE

    ref_nb_camions = 2
    ref_grid = [
        [01, 0, 0, 0, 2, 0, 0, 2, 0, 2, 2, 1, 0, 0, 1, 2],
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
        [2, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0],
    ]
    ref_width = 16
    ref_height = 15

    assert trucks.create_game(seed, filename) == (
        ref_nb_camions,
        ref_grid,
        ref_width,
        ref_height,
    )


def test_create_game_seed_5():
    seed = 5
    filename = MAP_FILE

    ref_nb_camions = 3
    ref_grid = [
        [2, 1, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 1, 0, 2],
        [0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 1, 0, 2, 1, 2],
        [0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 1, 1, 2, 2, 0, 0, 0],
        [0, 1, 1, 2, 0, 0, 0, 1, 0, 2, 2, 0, 1, 0, 1, 2, 2],
        [1, 1, 0, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 1, 0],
        [1, 1, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0],
        [0, 0, 0, 2, 0, 1, 1, 0, 0, 1, 0, 0, 1, 2, 2, 0, 0],
    ]
    ref_width = 17
    ref_height = 10

    assert trucks.create_game(seed, filename) == (
        ref_nb_camions,
        ref_grid,
        ref_width,
        ref_height,
    )


def test_truck_creation_0_0_0():
    camion = trucks.Camion(0, 0, 0)

    assert (camion._id, camion.x, camion.y) == (0, 0, 0)


def test_truck_creation_5_20_3():
    camion = trucks.Camion(5, 20, 3)

    assert (camion._id, camion.x, camion.y) == (5, 20, 3)


def test_truck_move_x_1(capsys):
    camion = trucks.Camion(0, 0, 0)

    camion.move(1, 0)

    captured = capsys.readouterr()
    assert captured.out == "0 MOVE 0 1 0\n"


def test_truck_move_diagonal(capsys):
    camion = trucks.Camion(0, 0, 0)

    camion.move(1, 1)

    captured = capsys.readouterr()
    assert captured.out == "0 MOVE 0 1 0\n"


def test_truck_dig_0_0(capsys):
    camion = trucks.Camion(0, 0, 0)
    camion.set_target(trucks.Crystal(0, 0, 1))

    camion.dig()

    captured = capsys.readouterr()
    assert captured.out == "0 DIG 0 0 0\n"


def test_truck_dig_25_4(capsys):
    camion = trucks.Camion(3, 25, 4)
    camion.set_target(trucks.Crystal(25, 4, 1))
    camion.nb_tour = 72
    camion.dig()

    capture = capsys.readouterr()
    assert capture.out == "72 DIG 3 25 4\n"


def test_truck_progress_dig_2(capsys):
    camion = trucks.Camion(0, 0, 0)
    camion.set_target(trucks.Crystal(0, 0, 2))

    trucks.GRID = [[2]]

    while trucks.GRID[0][0] > 0:
        camion.progress()
        capture = capsys.readouterr()
        assert capture.out == f"{camion.nb_tour-1} DIG 0 0 0\n"


def test_truck_zigzag_carre(capsys):
    trucks.WIDTH, trucks.HEIGHT = (2, 2)
    trucks.GRID = [[1, 1], [1, 1]]
    trucks.CRYSTALS = trucks.get_crystals_pos()
    expected = [
        "0 DIG 0 0 0",
        "1 MOVE 0 1 0",
        "2 DIG 0 1 0",
        "3 MOVE 0 1 1",
        "4 DIG 0 1 1",
        "5 MOVE 0 0 1",
        "6 DIG 0 0 1",
    ]

    trucks.one_truck_zigzag(trucks.Camion(0, 0, 0))
    capture = capsys.readouterr()
    assert capture.out.split("\n")[:-1] == expected


def test_nearest_basic(capsys):
    trucks.NB_TOUR = 0
    trucks.NB_CAMIONS = 1
    trucks.WIDTH, trucks.HEIGHT = (3, 3)
    trucks.GRID = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    trucks.CRYSTALS = trucks.get_crystals_pos()

    expected = [
        "0 DIG 0 0 0",
        "1 MOVE 0 1 0",
        "2 MOVE 0 1 1",
        "3 DIG 0 1 1",
        "4 MOVE 0 1 2",
        "5 DIG 0 1 2",
    ]

    trucks.all_trucks_nearest()
    capture = capsys.readouterr()
    assert capture.out.split("\n")[:-1] == expected


def test_nearest_angle(capsys):
    trucks.NB_TOUR = 0
    trucks.NB_CAMIONS = 1
    trucks.WIDTH, trucks.HEIGHT = (3, 3)
    trucks.GRID = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    trucks.CRYSTALS = trucks.get_crystals_pos()

    expected = [
        "0 DIG 0 0 0",
        "1 MOVE 0 1 0",
        "2 MOVE 0 2 0",
        "3 MOVE 0 2 1",
        "4 MOVE 0 2 2",
        "5 DIG 0 2 2",
    ]

    trucks.all_trucks_nearest()
    capture = capsys.readouterr()
    assert capture.out.split("\n")[:-1] == expected

    trucks.CRYSTALS = trucks.get_crystals_pos()


def test_get_nearest_crystal_easy():
    trucks.WIDTH, trucks.HEIGHT = (3, 3)
    trucks.GRID = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    
    trucks.CRYSTALS = trucks.get_crystals_pos()
    
    assert trucks.get_nearest_crystal(trucks.CRYSTALS, trucks.Camion(0, 0, 0)) == trucks.CRYSTALS["0:0"]
    
    
def test_get_nearest_crystal_further():
    trucks.WIDTH, trucks.HEIGHT = (3, 3)
    trucks.GRID = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]
    
    trucks.CRYSTALS = trucks.get_crystals_pos()
    
    assert trucks.get_nearest_crystal(trucks.CRYSTALS, trucks.Camion(0, 0, 0)) == trucks.CRYSTALS["1:2"]
    
    
    
def test_get_nearest_crystal_backward():
    trucks.WIDTH, trucks.HEIGHT = (3, 3)
    trucks.GRID = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    
    trucks.CRYSTALS = trucks.get_crystals_pos()
    
    assert trucks.get_nearest_crystal(trucks.CRYSTALS, trucks.Camion(0, 1, 1)) == trucks.CRYSTALS["0:0"]


def test_count_crystals_wo_bounds():
    trucks.WIDTH, trucks.HEIGHT = (3, 3)
    trucks.GRID = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    
    trucks.CRYSTALS = trucks.get_crystals_pos()
    
    assert trucks.count_crystals() == 3


def test_count_crystals_with_bounds():
    trucks.WIDTH, trucks.HEIGHT = (3, 3)
    trucks.GRID = [
        [1, 0, 0],
        [1, 2, 0],
        [1, 0, 1],
    ]
    
    trucks.CRYSTALS = trucks.get_crystals_pos()
    
    assert trucks.count_crystals([1, trucks.HEIGHT]) == 4