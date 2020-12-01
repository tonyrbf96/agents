from .enviroment import Enviroment
from .object import EnviromentObject
from .util import Position


class Agent(EnviromentObject):
    def update(self, enviroment: Enviroment):
        pass


class BaseBaby(Agent):
    def __init__(self, position: Position):
        super().__init__(position)
        self.previous_position: Position = self.position
        self.in_corral = False


class BaseRobot(Agent):
    def __init__(self, position: Position):
        super().__init__(position)
        self.baby: "BaseBaby|None" = None
