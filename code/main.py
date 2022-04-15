from contextlib import redirect_stdout
import pathlib
import game
import argparse
import sys

FILENAME = "map.txt"

GRID_OPEN = "### Grid ###"
GRID_CLOSE = "### End Grid ###"

def generate_map(filename):
    with open(filename, 'w') as f:
        with redirect_stdout(f):
            game.init_game(4)
           
def parse_map(filename):
    map = []
    
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
                map.append([x for x in line.rstrip("\n").replace(" ", "0")])                   

    return map

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
    
    print(parse_map(filename))
    print("test")
    