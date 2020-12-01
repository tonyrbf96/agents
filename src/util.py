from random import Random, randint, shuffle
from typing import Tuple

DEBUG = True


class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, o: "Position"):
        return Position(self.x + o.x, self.y + o.y)

    def __sub__(self, o: "Position"):
        return Position(self.x - o.x, self.y - o.y)

    def __mul__(self, o: int):
        return Position(self.x * o, self.y * o)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.x, self.y))

    def length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5


def get_all_positions(x_max, y_max):
    positions: "list[Position]" = []
    for x in range(x_max):
        for y in range(y_max):
            positions.append(Position(x, y))
    return positions


def get_random_all_positions(x_max, y_max):
    ls = get_all_positions(x_max, y_max)
    shuffle(ls)
    return ls


def get_random_adyacents(position: Position):
    ls = get_adyacents(position)
    shuffle(ls)
    return ls


def get_adyacents(position: Position) -> "list[Position]":
    dirs: "list[Tuple[int , int]]" = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            dirs.append((x, y))
    dirs.remove((0, 0))
    return [Position(position.x + x, position.y + y) for x, y in dirs]
