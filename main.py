import src.main
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", type=int)
    parser.add_argument("name", type=str)

    args = parser.parse_args()

    seed = args.seed
    filename = args.name

    src.main.main(seed, filename)
