from src.enviroment import Enviroment

from .object import EnviromentObject


class Agent(EnviromentObject):
    def update(self, enviroment: Enviroment):
        pass


class Baby(Agent):
    pass


class Robot(Agent):
    pass
