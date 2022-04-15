# transcription of the original game.c/game.h files

MAX_NB_TRUCKS = 9
MAX_WIDTH = 30
MAX_HEIGHT = 20

# https://en.wikipedia.org/wiki/Linear_congruential_generator glibc
_MODULUS = 1 << 31
_MULTIPLIER = 1103515245
_INCREMENT = 12345

_prng = 0


def srand(seed: int) -> None:
    global _prng
    _prng = seed


def rand() -> int:
    global _prng
    _prng = (_MULTIPLIER * _prng + _INCREMENT) % _MODULUS
    return _prng & 0x7FFFFFFF


def init_game(seed: int):
    srand(seed)
    cristals = []
    nb_trucks = rand() % (MAX_NB_TRUCKS - 1) + 1
    width = rand() % (MAX_WIDTH - 10) + 10
    height = rand() % (MAX_HEIGHT - 10) + 10
    for y in range(height):
        for x in range(width):
            nb_crystals = rand() % 5
            if nb_crystals < 3:
                cristals.append(nb_crystals)
            else:
                cristals.append(0)
    print(f"trucks: {nb_trucks}")
    print(f"width: {width}")
    print(f"height: {height}")
    display_cristals(width, height, cristals)
    print("\nStart!")


def display_cristals(width, height, cristals):
    print("\n### Grid ###")
    for y in range(height):
        for x in range(width):
            nb_cristals = cristals[x + y * width]
            if nb_cristals:
                print(nb_cristals, end="")
            else:
                print(" ", end="")
        print()
    print("### End Grid ###")