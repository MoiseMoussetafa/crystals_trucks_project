from contextlib import redirect_stdout
import pathlib
from src import game
import sys

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
    def __init__(self, id, x, y) -> None:
        self._id = id
        self.x = x
        self.y = y

    def move(self, x, y):
        global GRID
        global NB_TOUR

        if self.x != x or self.y != y:
            self.x = x
            self.y = y
            print(f"{NB_TOUR} MOVE {self._id} {x} {y}")
            NB_TOUR += 1

        while GRID[self.y][self.x] > 0:
            self.dig()
            GRID[self.y][self.x] -= 1

    def dig(self):
        global NB_TOUR
        print(f"{NB_TOUR} DIG {self._id} {self.x} {self.y}")
        NB_TOUR += 1


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
    global NB_CAMIONS, GRID, WIDTH, HEIGHT

    NB_CAMIONS, GRID, WIDTH, HEIGHT = create_game(seed, filename)
    if not pathlib.Path(filename).exists():
        print("File not found.")
        sys.exit(-1)

    camion = Camion(0, 0, 0)

    print(NB_CAMIONS, WIDTH, HEIGHT)
    print(GRID)

    with open(filename, 'a') as f:
        with redirect_stdout(f):
            index_y = 0
            while index_y < HEIGHT:
                for index_x in range(0, WIDTH, 1):
                    camion.move(index_x, index_y)

                if index_y < HEIGHT-1:
                    index_y += 1
                else:
                    break

                for index_x in range(WIDTH-1, -1, -1):
                    camion.move(index_x, index_y)

                if index_y < HEIGHT-1:
                    index_y += 1
                else:
                    break
