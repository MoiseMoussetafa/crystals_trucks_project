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


class Camion:
    global NB_TOUR
    global GRID

    def __init__(self, id, x, y) -> None:
        self._id = id
        self.x = x
        self.y = y
        self.has_target = False
        self.target_x, self.target_y = 0, 0

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

    def set_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y
        self.has_target = True

    def progress(self):
        if self.has_target:
            if self.target_x == self.x and self.target_y == self.y:
                if GRID[self.y][self.x] > 0:
                    self.dig()
                    GRID[self.y][self.x] -= 1
                if GRID[self.y][self.x] == 0:
                    self.has_target = False
            else:
                self.move(self.target_x, self.target_y)


def create_game(seed: int, filename: str) -> tuple:
    grid = []

    with open(filename, 'w') as f:
        with redirect_stdout(f):
            game.init_game(seed)

    with open(filename, 'r') as f:
        is_in_grid = False
        for line in f.readlines():
            if GRID_OPEN in line:
                is_in_grid = True
                continue
            elif GRID_CLOSE in line:
                is_in_grid = False
                continue

            if is_in_grid:
                grid.append([
                    int(x) for x in line.rstrip("\n").replace(" ", "0")])
            elif CAMIONS_FLAG in line:
                nb_camions = int(
                    line.translate([" \n", ""]).lstrip(CAMIONS_FLAG))
            elif WIDTH_FLAG in line:
                width = int(line.translate([" \n", ""]).lstrip(WIDTH_FLAG))
            elif HEIGHT_FLAG in line:
                height = int(line.translate([" \n", ""]).lstrip(HEIGHT_FLAG))

    return nb_camions, grid, width, height


def main(seed, filename):
    global NB_CAMIONS, GRID, WIDTH, HEIGHT, NB_TOUR

    NB_CAMIONS, GRID, WIDTH, HEIGHT = create_game(seed, filename)
    if not pathlib.Path(filename).exists():
        print("File not found.")
        sys.exit(-1)

    camion = Camion(0, 0, 0)

    with open(filename, 'a') as f:
        with redirect_stdout(f):
            index_y = 0
            while index_y < HEIGHT:
                for index_x in itertools.chain(
                        range(0, WIDTH, 1), range(WIDTH, -2, -1)):
                    if index_x == WIDTH:
                        index_y += 1
                        index_x -= 1
                    elif index_x == -1:
                        index_y += 1
                        index_x += 1
                    if index_y >= HEIGHT:
                        break

                    if GRID[index_y][index_x] > 0:
                        camion.set_target(index_x, index_y)

                    while GRID[index_y][index_x] > 0:
                        camion.progress()
                        NB_TOUR += 1
