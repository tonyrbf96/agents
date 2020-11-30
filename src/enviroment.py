from src.util import Position

from .object import Corral, Dirt, EnviromentObject, Obstacle  # noqa: F401


class Enviroment:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.objects: "list[EnviromentObject]" = []

    def find(self, pos: Position) -> "list[EnviromentObject]":
        result: "list[EnviromentObject]" = []
        for obj in self.objects:
            if obj.position.x == pos.x and obj.position.y == pos.y:
                result.append(obj)

        return result

    def is_valid(self, pos: Position):
        return pos.x > 0 and pos.x < self.width and pos.y > 0 and pos.x < self.height
