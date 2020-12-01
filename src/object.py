from .util import Position


class EnviromentObject:
    def __init__(self, position: Position = Position(0, 0)):
        self.position: Position = position

    def __str__(self):
        return f"({self.position.x},{self.position.y})"


class Corral(EnviromentObject):
    pass


class Dirt(EnviromentObject):
    pass
