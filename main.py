import src.trucks
import argparse
import sys


def main(seed, filename):
    return src.trucks.main(seed, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", type=int)
    parser.add_argument("name", type=str)

    args = parser.parse_args()

    seed = args.seed
    filename = args.name

    sys.exit(main(seed, filename))
