from random import Random
from typing import Tuple


class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def get_adyacents(self):
        dirs: "list[Tuple[int , int]]" = []

        for x in range(-1, 2):
            for y in range(-1, 2):
                dirs.append((x, y))

        dirs.remove((0, 0))
        return [Position(self.x + x, self.y + y) for x, y in dirs]

    def move(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o: "Position"):
        return Position(self.x + o.x, self.y + o.y)

    def __sub__(self, o: "Position"):
        return Position(self.x - o.x, self.y - o.y)

    def __mul__(self, o: int):
        return Position(self.x * o, self.y * o)


def get_random_position(x_max, y_max):
    positions: "list[Tuple[int, int]]" = []
    for x in range(x_max):
        for y in range(y_max):
            positions.append((x, y))
    random = Random()
    for _ in range(x_max * y_max):
        i: int = random.randint(0, len(positions) - 1)
        yield Position(*positions[i])
        positions.pop(i)
