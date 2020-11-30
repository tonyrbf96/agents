from random import randint

from .agent import Baby, Robot
from .enviroment import Enviroment
from .object import Dirt
from .util import Position


class ReactiveBaby(Baby):
    def update(self, data: Enviroment):
        positions = self.position.get_adyacents()
        for _ in range(len(positions)):
            pos = positions.pop(randint(0, len(positions) - 1))
            dir = self.position - pos

    def is_valid_to_move(self, pos: Position, enviroment: Enviroment):
        if enviroment.is_valid(pos):
            return all(
                [
                    not (type(obj) is Robot or type(obj) is Baby or type(obj) is Dirt)
                    for obj in enviroment.find(pos)
                ]
            )
        return False
