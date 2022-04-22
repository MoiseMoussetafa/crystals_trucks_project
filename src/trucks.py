from contextlib import redirect_stdout
import pathlib
from src import game
import sys
import itertools

CAMIONS_FLAG = "trucks:"
WIDTH_FLAG = "width:"
HEIGHT_FLAG = "height:"
GRID_OPEN = "### Grid ###"
GRID_CLOSE = "### End Grid ###"

NB_CAMIONS = 0
GRID = None
WIDTH = 0
HEIGHT = 0

NB_TOUR = 0


class Crystal:
    def __init__(self, x, y, count) -> None:
        self.x = x
        self.y = y
        self.count = count

    def dig(self):
        global GRID
        self.count -= 1
        GRID[self.y][self.x] -= 1


class Camion:
    global NB_TOUR

    def __init__(self, id, x, y) -> None:
        self._id = id
        self.x = x
        self.y = y
        self.target = None

    def move(self, x, y):
        if x > self.x:
            self.x += 1
        elif x < self.x:
            self.x -= 1
        elif y > self.y:
            self.y += 1
        elif y < self.y:
            self.y -= 1
        print(f"{NB_TOUR} MOVE {self._id} {self.x} {self.y}")

    def dig(self):
        print(f"{NB_TOUR} DIG {self._id} {self.x} {self.y}")
        self.target.dig()

    def set_target(self, crystal: Crystal):
        self.target = crystal

    def progress(self):
        if self.target:
            if self.target.x == self.x and self.target.y == self.y:
                if self.target.count > 0:
                    self.dig()
                if self.target.count == 0:
                    del self.target
                    self.target = None
            else:
                self.move(self.target.x, self.target.y)


def create_game(seed: int, filename: str) -> tuple:
    grid = []

    with open(filename, "w") as f:
        with redirect_stdout(f):
            game.init_game(seed)

    with open(filename, "r") as f:
        is_in_grid = False
        for line in f.readlines():
            if GRID_OPEN in line:
                is_in_grid = True
                continue
            elif GRID_CLOSE in line:
                is_in_grid = False
                continue

            if is_in_grid:
                grid.append([int(x) for x in line.rstrip("\n").replace(" ", "0")])
            elif CAMIONS_FLAG in line:
                nb_camions = int(line.translate([" \n", ""]).lstrip(CAMIONS_FLAG))
            elif WIDTH_FLAG in line:
                width = int(line.translate([" \n", ""]).lstrip(WIDTH_FLAG))
            elif HEIGHT_FLAG in line:
                height = int(line.translate([" \n", ""]).lstrip(HEIGHT_FLAG))

    return nb_camions, grid, width, height


def get_crystals_pos():
    global GRID, WIDTH, HEIGHT

    crystals = {}

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if GRID[y][x] > 0:
                crystals[f"{x}:{y}"] = Crystal(x, y, GRID[y][x])

    return crystals


def one_truck_zigzag():
    global GRID, WIDTH, HEIGHT, NB_TOUR

    truck = Camion(0, 0, 0)
    crystals = get_crystals_pos()

    index_y = 0
    while index_y < HEIGHT:
        for index_x in itertools.chain(range(0, WIDTH, 1), range(WIDTH, -2, -1)):
            if index_x == WIDTH:
                index_y += 1
                index_x -= 1
            elif index_x == -1:
                index_y += 1
                index_x += 1
            if index_y >= HEIGHT:
                break

            if f"{index_x}:{index_y}" in crystals.keys():
                truck.set_target(crystals[f"{index_x}:{index_y}"])

                while crystals[f"{index_x}:{index_y}"].count > 0:
                    truck.progress()
                    NB_TOUR += 1


def all_trucks_zigzag() -> None:
    global NB_CAMIONS, GRID, WIDTH, HEIGHT, NB_TOUR

    trucks = []
    for i in range(NB_CAMIONS):
        trucks.append(Camion(i, 0, i))


def main(seed, filename):
    global NB_CAMIONS, GRID, WIDTH, HEIGHT, NB_TOUR

    NB_CAMIONS, GRID, WIDTH, HEIGHT = create_game(seed, filename)
    if not pathlib.Path(filename).exists():
        print("File not found.")
        sys.exit(-1)

    with open(filename, "a") as f:
        with redirect_stdout(f):
            one_truck_zigzag()
