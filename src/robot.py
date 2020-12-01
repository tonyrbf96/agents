from typing import Type, cast

from .agent import Agent, BaseBaby, BaseRobot
from .calculation import calculate_dirty
from .enviroment import Enviroment
from .object import Corral, Dirt
from .obstacle import Obstacle
from .util import Position, get_adyacents, get_all_positions, get_random_adyacents


class Robot(BaseRobot):
    def get_random_valid_adyacent_position(self, enviroment: Enviroment):
        positions = get_random_adyacents(self.position)
        for pos in positions:
            if self.is_valid_to_move(pos, enviroment):
                return pos
        return self.position

    def update(self, enviroment: Enviroment):
        if enviroment.has(self.position, Dirt):
            self.clean(enviroment)
            return

        pos = self.get_random_valid_adyacent_position(enviroment)
        self.move(pos, enviroment)

    def is_valid_to_move(self, pos: Position, enviroment: Enviroment):
        if enviroment.is_valid(pos):
            return all(
                [
                    not (
                        issubclass(type(obj), Obstacle)
                        or issubclass(type(obj), BaseRobot)
                        or (
                            issubclass(type(obj), BaseBaby)
                            and enviroment.has(pos, Corral)
                        )
                        or (self.baby and issubclass(type(obj), BaseBaby))
                        # just get one baby
                    )
                    for obj in enviroment.find_at(pos)
                ]
            )
        return False

    def move(self, pos: Position, enviroment: Enviroment):
        # print("Robot: move")
        self.position = pos

        # Pick up a baby
        baby = enviroment.get_at(pos, BaseBaby)
        if baby is not None:
            self.baby = cast(type(BaseBaby), baby)
            # print("Robot: pick up")

        # Move the baby
        if self.baby is not None:
            self.baby.position = pos

    def clean(self, enviroment: Enviroment):
        dirt = enviroment.get_at(self.position, Dirt)
        assert dirt is not None
        enviroment.objects.remove(dirt)
        # print("Robot: clean")

    def drop(self, enviroment: Enviroment):
        self.baby.in_corral = True
        self.baby = None
        # print("Robot: drop")

    def go_to_corral(self, enviroment: Enviroment):
        # print("Robot: to corral")
        corrals = enviroment.search_by_type([Corral])
        for c in corrals:
            if not self.is_valid_to_move(c.position, enviroment):
                continue
            path = self.get_valid_path_to(self.position, c.position, enviroment)
            if not path:
                continue
            self.move(path.pop(0), enviroment)

            if len(path) == 0:
                return

            if enviroment.has(self.position, Dirt):
                self.clean(enviroment)
                return
            else:
                self.move(path[0], enviroment)
                return

    def get_valid_path_to(self, origin: Position, to: Position, enviroment: Enviroment):
        grid: "list[list[int]]" = []
        grid = [[0 for _ in range(enviroment.height)] for _ in range(enviroment.width)]
        grid[origin.x][origin.y] = 1

        pather: "dict[Position, Position| None]" = {}
        pather[origin] = None

        pending: "list[Position]" = []
        pending.append(origin)
        while len(pending) > 0:
            c = pending.pop()
            founded = False
            for p in get_adyacents(c):
                if self.is_valid_to_move(p, enviroment):
                    if grid[p.x][p.y] == 0:
                        grid[p.x][p.y] = grid[c.x][c.y] + 1
                        pather[p] = c
                        pending.insert(0, p)
                        if p == to:
                            founded = True
                            break
            if founded:
                break
        # for row in grid:
        #     print(row)
        # print("\n")
        if to not in pather:
            return None

        def recursive_add(p):
            if pather[p] is None:
                return []
            else:
                return recursive_add(pather[p]) + [p]

        return recursive_add(to)


class ReactiveRobot(Robot):
    def update(self, enviroment: Enviroment):
        if enviroment.has(self.position, Dirt):
            self.clean(enviroment)
            return

        if self.baby is not None and enviroment.has(self.position, Corral):
            self.drop(enviroment)
            return

        if self.baby is not None:
            self.go_to_corral(enviroment)
            return

        pos = self.get_random_prefered_valid_adyacent_position(enviroment)
        self.move(pos, enviroment)

    def get_random_prefered_valid_adyacent_position(self, enviroment: Enviroment):
        positions = get_random_adyacents(self.position)
        random_prefered_positions = list(
            filter(
                lambda p: self.is_valid_to_move(p, enviroment),
                positions,
            )
        )
        random_prefered_positions.sort(
            key=lambda x: 2
            if enviroment.has(x, Corral)
            else 0
            if enviroment.has(x, BaseBaby)
            else 1
            if enviroment.has(x, Dirt)
            else 2
        )

        if random_prefered_positions:
            return random_prefered_positions[0]
        else:
            return self.position


class GoalRobot(ReactiveRobot):
    def update(self, enviroment: Enviroment):
        dirty = calculate_dirty(enviroment)

        if self.baby is not None and enviroment.has(self.position, Corral):
            self.drop(enviroment)
            return

        if self.baby is not None:
            self.go_to_corral(enviroment)
            return

        if enviroment.has(self.position, Dirt):
            self.clean(enviroment)
            return

        if dirty > 25:
            if self.lookfor_babies(enviroment):
                return

        self.lookfor_dirt(enviroment)

    def search_nearest(self, enviroment: Enviroment, filter: Type):
        objs = enviroment.search_by_type([filter])
        objs.sort(key=lambda obj: (obj.position - self.position).length())
        return objs

    def lookfor_babies(self, enviroment):
        babies = self.search_nearest(enviroment, BaseBaby)
        for baby in babies:
            if baby.in_corral:
                continue
            path = self.get_valid_path_to(self.position, baby.position, enviroment)
            if not path:
                continue
            self.move(path.pop(0), enviroment)
            return True
        return False

    def lookfor_dirt(self, enviroment):
        dirt = self.search_nearest(enviroment, Dirt)
        for d in dirt:
            path = self.get_valid_path_to(self.position, d.position, enviroment)
            if not path:
                continue
            self.move(path.pop(0), enviroment)
            return
