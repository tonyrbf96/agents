from src.util import Position

from .enviroment import Enviroment
from .object import EnviromentObject


class Obstacle(EnviromentObject):
    def try_move(self, dir: Position, enviroment: Enviroment):
        pos = self.position + dir
        if enviroment.is_valid(pos):  # outside the enviroment
            objs = enviroment.find_at(pos)
            if not objs:  # a free position
                self.position = pos
                return True
            for obj in objs:
                if not type(obj) is Obstacle:  # if are not a obstacle
                    return False
                elif obj.try_move(dir, enviroment):  # there are just one object
                    self.position = pos
                    return True
        else:
            return False
