from contextlib import redirect_stdout
import pathlib
import game
import argparse
import sys

FILENAME = "map.txt"

CAMIONS_FLAG = "trucks:"
GRID_OPEN = "### Grid ###"
GRID_CLOSE = "### End Grid ###"

NB_CAMIONS = 0
GRID = None

class Camion:
    def __init__(self, id, x, y) -> None:
        self._id = id
        self.x = x
        self.y = y

    def move(self, tour_id, x, y):
        global GRID
        
        if self.x != x or self.y != self.y:
            self.x = x
            self.y = y
            print(f"{tour_id} MOVE {self._id} {x} {y}")
        
        while GRID[y][x] > 0:
            self.dig(tour_id)
            GRID[y][x] -= 1
            tour_id += 1
        
    def dig(self, tour_id):
        print(f"{tour_id} DIG {self._id} {self.x} {self.y}")
        

def generate_map(filename):
    with open(filename, 'w') as f:
        with redirect_stdout(f):
            game.init_game(4)
           
def parse_game(filename):
    grid = []
    
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
                grid.append([int(x) for x in line.rstrip("\n").replace(" ", "0")])
            elif CAMIONS_FLAG in line:
                nb_camions = int(line.translate([" \n", ""]).lstrip(CAMIONS_FLAG))

    return nb_camions, grid

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", type=str)
    
    args = parser.parse_args()
    
    if args.map:
        filename = args.map
    else:
        generate_map(FILENAME)
        filename = FILENAME
    
    if not pathlib.Path(filename).exists():
        print("File not found.")
        sys.exit(-1)    
    
    NB_CAMIONS, GRID = parse_game(filename)
    tab_camion = []
    for i in range NB_CAMIONS:
        tab_camion[i] = Camion(i,0,i) 
    
    print(tab_camion)
    print(NB_CAMIONS)
    
    with open(filename, 'a') as f:
        with redirect_stdout(f):
            tour = 0
            for index_y, y in enumerate(GRID):
                for index_x, x in enumerate(y):
                    camion.move(tour, index_x, index_y)
                    tour += 1