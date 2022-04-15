from contextlib import redirect_stdout
import pathlib
import game
import argparse
import sys

FILENAME = "map.txt"

GRID_OPEN = "### Grid ###"
GRID_CLOSE = "### End Grid ###"

GRID = None

class Camion:
    def __init__(self, id, x, y) -> None:
        self._id = id
        self.x = x
        self.y = y

    def move(self, x, y):
        global GRID
        self.x = x
        self.y = y
        print(f"0 MOVE {self._id} {x} {y}")
        
        while GRID[y][x] > 0:
            self.dig()
            GRID[y][x] -= 1
        
    def dig(self):
        print(f"0 DIG {self._id} {self.x} {self.y}")
        

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

    return grid

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
    
    GRID = parse_game(filename)
    camion = Camion(0, 0, 0)
    
    with open(filename, 'a') as f:
        with redirect_stdout(f):
            for index_y, y in enumerate(GRID):
                for index_x, x in enumerate(y):
                    camion.move(index_x, index_y)