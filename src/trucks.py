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
CRYSTALS = {}


class Crystal:
    global GRID, CRYSTALS

    def __init__(self, x, y, count) -> None:
        self.x = x
        self.y = y
        self.count = count
        self.targeted_by = None

    def dig(self):
        self.count -= 1

        if GRID:
            GRID[self.y][self.x] -= 1

    def distance_from(self, x, y):
        return abs(self.x - x) + abs(self.y - y)


class Camion:
    def __init__(self, id, x, y) -> None:
        self._id = id
        self.x = x
        self.y = y
        self.target_list = []
        self.target = None
        self.nb_tour = 0

    def move(self, x, y):
        if x > self.x:
            self.x += 1
        elif x < self.x:
            self.x -= 1
        elif y > self.y:
            self.y += 1
        elif y < self.y:
            self.y -= 1
        print(f"{self.nb_tour} MOVE {self._id} {self.x} {self.y}")

    def dig(self):
        print(f"{self.nb_tour} DIG {self._id} {self.x} {self.y}")
        self.target.dig()

    def set_target(self, crystal: Crystal):
        if crystal:
            self.target = crystal
            crystal.targeted_by = self._id

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
            self.nb_tour += 1


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


def one_truck_zigzag(truck, bounds=None):
    global WIDTH, HEIGHT, CRYSTALS

    if not bounds:
        bounds = [0, HEIGHT]

    index_y = bounds[0]
    while index_y < bounds[1]:
        for index_x in itertools.chain(range(0, WIDTH, 1), range(WIDTH, -2, -1)):
            if index_x == WIDTH:
                index_y += 1
                index_x -= 1
            elif index_x == -1:
                index_y += 1
                index_x += 1
            if index_y >= bounds[1]:
                break

            if f"{index_x}:{index_y}" in CRYSTALS.keys():
                truck.set_target(CRYSTALS[f"{index_x}:{index_y}"])

                while CRYSTALS[f"{index_x}:{index_y}"].count > 0:
                    truck.progress()


def all_trucks_zigzag() -> None:
    global NB_CAMIONS, GRID, WIDTH, HEIGHT

    div_height = HEIGHT // NB_CAMIONS
    bottom = 0
    top = div_height
    for i in range(NB_CAMIONS):
        one_truck_zigzag(Camion(i, 0, i), [bottom, top])
        bottom += div_height

        if i == NB_CAMIONS - 2:
            top = HEIGHT
        else:
            top = bottom + div_height


def get_nearest_crystal(crystals, truck):
    sorted_crystals = sorted(
        crystals.values(), key=lambda c: c.distance_from(truck.x, truck.y)
    )
    for i in range(1, len(sorted_crystals)):
        if (
            sorted_crystals[i].distance_from(truck.x, truck.y)
            == sorted_crystals[i - 1].distance_from(truck.x, truck.y)
            and sorted_crystals[i].x < sorted_crystals[i - 1].x
        ):
            sorted_crystals[i], sorted_crystals[i - 1] = (
                sorted_crystals[i - 1],
                sorted_crystals[i],
            )

    for target in sorted_crystals:
        if target.targeted_by is None or target.targeted_by == truck._id:
            return target

    return sorted_crystals[0]


def one_truck_nearest(truck, bounds=None):
    global WIDTH, HEIGHT, CRYSTALS

    if not bounds:
        bounds = [0, HEIGHT]

    crystals = {}
    for y in range(bounds[0], bounds[1]):
        for x in range(WIDTH):
            if f"{x}:{y}" in CRYSTALS.keys():
                crystals[f"{x}:{y}"] = CRYSTALS[f"{x}:{y}"]

    if len(crystals) > 0:
        if f"{truck.x}:{truck.y}" in CRYSTALS.keys():
            target = CRYSTALS[f"{truck.x}:{truck.y}"]
        else:
            target = get_nearest_crystal(crystals, truck)

        truck.set_target(target)

        if target.count > 0:
            truck.progress()
        if target.count == 0:
            CRYSTALS.pop(f"{target.x}:{target.y}")


def count_crystals(bounds=None):
    global GRID, WIDTH, HEIGHT, CRYSTALS

    count = 0

    if not bounds:
        bounds = [0, HEIGHT]

    for y in range(bounds[0], bounds[1]):
        for x in range(WIDTH):
            if f"{x}:{y}" in CRYSTALS.keys():
                count += 1

    return count


def all_trucks_nearest() -> None:
    global NB_CAMIONS, GRID, WIDTH, HEIGHT, CRYSTALS

    trucks = []
    for i in range(NB_CAMIONS):
        trucks.append(Camion(i, 0, i))

    while len(CRYSTALS) > 0:
        div_height = (HEIGHT // NB_CAMIONS) + 1
        bottom = 0
        top = div_height
        for i in range(NB_CAMIONS):
            bounds = [bottom, top]

            if trucks[i].target and trucks[i].target.count == 0:
                trucks[i].target = None

            if count_crystals(bounds) == 0:
                bounds = None

            one_truck_nearest(trucks[i], bounds)
            bottom += div_height

            if i == NB_CAMIONS - 2:
                top = HEIGHT
            else:
                top = bottom + div_height


def main(seed, filename):
    global NB_CAMIONS, GRID, WIDTH, HEIGHT, CRYSTALS

    NB_CAMIONS, GRID, WIDTH, HEIGHT = create_game(seed, filename)
    if not pathlib.Path(filename).exists():
        print("File not found.")
        sys.exit(-1)

    CRYSTALS = get_crystals_pos()
    # one_truck_nearest(Camion(0, 0, 0))

    truck = Camion(0, 0, 0)

    with open(filename, "a") as f:
        with redirect_stdout(f):
            # one_truck_zigzag(Camion(0, 0, 0))
            # all_trucks_zigzag()

            # while len(CRYSTALS) > 0:
            #     one_truck_nearest(truck)

            all_trucks_nearest()

    sys.exit(0)
