from typing import Type

from .object import EnviromentObject  # noqa: F401
from .util import Position


class Enviroment:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.objects: "list[EnviromentObject]" = []

    def find_at(self, pos: Position) -> "list[EnviromentObject]":
        result: "list[EnviromentObject]" = []

        for obj in self.objects:
            if obj.position.x == pos.x and obj.position.y == pos.y:
                result.append(obj)

        return result

    def search_by_type(self, filters: "list[Type]" = []):
        result: "list[EnviromentObject]" = []
        for obj in self.objects:
            if filters and not any(
                [issubclass(type(obj), filter) for filter in filters]
            ):
                continue
            result.append(obj)
        return result

    def get_at(self, pos: Position, filter: Type):
        for obj in self.find_at(pos):
            if issubclass(type(obj), filter):
                return obj
        return None

    def has(self, pos: Position, filter: Type):
        return self.get_at(pos, filter) is not None

    def is_valid(self, pos: Position):
        return pos.x >= 0 and pos.x < self.width and pos.y >= 0 and pos.y < self.height
