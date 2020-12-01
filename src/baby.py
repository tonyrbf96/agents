from .agent import BaseBaby, BaseRobot
from .enviroment import Enviroment
from .object import Corral, Dirt
from .obstacle import Obstacle
from .util import Position, get_random_adyacents


class Baby(BaseBaby):
    def update(self, enviroment: Enviroment):

        # If the baby is taked by a robot or is in the corral
        if enviroment.get_at(self.position, BaseRobot) is not None or self.in_corral:
            return

        # find a nice place to move
        positions = get_random_adyacents(self.position)
        for pos in positions:
            if self.is_valid_to_move(pos, enviroment):
                objs = enviroment.find_at(pos)
                # It is free, lets move!
                if not objs:
                    self.move(pos, enviroment)
                # Try to move the obstacles
                for obj in objs:
                    if type(obj) is Obstacle:
                        if obj.try_move(pos - self.position, enviroment):
                            self.move(pos, enviroment)
                break

    def is_valid_to_move(self, pos: Position, enviroment: Enviroment):
        if enviroment.is_valid(pos):
            return all(
                [
                    not (
                        issubclass(type(obj), BaseRobot)
                        or issubclass(type(obj), Baby)
                        or issubclass(type(obj), Dirt)
                    )
                    for obj in enviroment.find_at(pos)
                ]
            )
        return False

    def move(self, pos: Position, enviroment):
        self.previous_position = self.position
        self.position = pos
        self.make_dirty(enviroment)

    def make_dirty(self, enviroment: Enviroment):
        # There is or a robot or in corral, no generate dirt
        if len(enviroment.find_at(self.position)) > 1:
            return
        grid = list(get_random_adyacents(self.previous_position))
        if self.position in grid:
            grid.remove(self.position)
        i = 1
        for p in grid:
            objs = enviroment.find_at(p)
            if objs and all([issubclass(type(obj), BaseBaby) for obj in objs]):
                i += 1
        amount = 1 if i == 1 else 3 if i == 2 else 6 if i > 2 else 0
        for p in grid:
            if amount <= 0:
                break
            if len(enviroment.find_at(p)) == 0:
                enviroment.objects.append(Dirt(p))
                amount -= 1
