from random import Random, randint
from typing import Callable, cast

from .agent import BaseBaby, BaseRobot
from .calculation import calculate_dirty
from .enviroment import Enviroment
from .object import Corral, Dirt, EnviromentObject  # noqa: F401
from .obstacle import Obstacle
from .util import (
    DEBUG,
    Position,
    get_all_positions,
    get_random_adyacents,
    get_random_all_positions,
)


class Simulation:
    def __init__(
        self,
        t: int,
        total_time: int,
        width: int,
        height: int,
        obstacle_percent: int,
        dirty_percent: int,
        robot_count: int,
        robot_factory: "Callable[[Position],BaseRobot]",
        baby_count: int,
        baby_factory: "Callable[[Position],BaseBaby]",
    ):
        self.time = t
        self.total_time = total_time
        self.width = width
        self.height = height

        self.obstacle_percent = obstacle_percent
        self.dirty_percent = dirty_percent

        self.robot_count = robot_count
        self.robot_factory = robot_factory

        self.baby_count = baby_count
        self.baby_factory = baby_factory

        self.max_percent = 0
        self.victory = False
        self.fail = False
        self.percents = []

    def __generate_enviroment(self, dirty_count=-1, obstacle_count=-1):
        enviroment: Enviroment = Enviroment(self.width, self.height)

        positions = list(
            get_random_all_positions(self.width, self.height)
        )  # All avalidable positions

        for _ in range(self.robot_count):
            robot = self.robot_factory(positions.pop())
            enviroment.objects.append(robot)

        for _ in range(self.baby_count):
            baby = self.baby_factory(positions.pop())
            enviroment.objects.append(baby)

        # Corrals
        corrals: "list[Corral]" = []
        for _ in range(self.baby_count):
            if not corrals:
                corrals.append(Corral(positions.pop()))
            else:
                for c in corrals:
                    corral_created = False
                    for p in get_random_adyacents(c.position):
                        if (
                            enviroment.is_valid(p)
                            and len(enviroment.find_at(p)) == 0
                            and p in positions
                        ):
                            corrals.append(Corral(p))
                            positions.remove(p)
                            corral_created = True
                            break
                    if corral_created:
                        break
        for c in corrals:
            enviroment.objects.append(c)

        # Dirt
        total = self.width * self.height
        for _ in range(
            self.dirty_percent * total // 100 if dirty_count == -1 else dirty_count
        ):
            if positions:
                enviroment.objects.append(Dirt(positions.pop()))

        # Obstacle
        for _ in range(
            self.obstacle_percent * total // 100
            if dirty_count == -1
            else obstacle_count
        ):
            if positions:
                enviroment.objects.append(Obstacle(positions.pop()))
        return enviroment

    def __shunffle_enviroment(self, enviroment: Enviroment):
        in_corrals = len(
            list(
                filter(
                    lambda b: cast(BaseBaby, b).in_corral,
                    enviroment.search_by_type([BaseBaby]),
                )
            )
        )
        in_robots = len(
            list(
                filter(
                    lambda b: cast(BaseRobot, b).baby is not None,
                    enviroment.search_by_type([BaseRobot]),
                )
            )
        )
        dirty_count = len(enviroment.search_by_type([Dirt]))
        obstacle_count = len(enviroment.search_by_type([Obstacle]))
        new_enviroment = self.__generate_enviroment(dirty_count, obstacle_count)

        babies = new_enviroment.search_by_type([BaseBaby])
        robots = new_enviroment.search_by_type([BaseRobot])
        corrals = new_enviroment.search_by_type([Corral])

        for _ in range(in_corrals):
            corral = corrals.pop()
            baby = babies.pop()
            cast(BaseBaby, baby).in_corral = True
            baby.position = corral.position

        for _ in range(in_robots):
            robot = robots.pop()
            baby = babies.pop()
            cast(BaseRobot, robot).baby = baby
            baby.position = robot.position

    def start_simulation(self):
        enviroment = self.__generate_enviroment()

        for i in range(self.total_time):
            for j in range(self.time):
                self.update(enviroment)
                percent = calculate_dirty(enviroment)
                self.percents.append(percent)

                if percent >= 60:
                    self.fail = True
                    return
                if self.win(enviroment):
                    self.victory = True
                    return
            self.__shunffle_enviroment(enviroment)
        # if DEBUG:
        #     self.print_grid(enviroment)

    def win(self, enviroment: Enviroment):
        return (
            all(
                [
                    cast(BaseBaby, baby).in_corral
                    for baby in enviroment.search_by_type([BaseBaby])
                ]
            )
            and enviroment.search_by_type([Dirt]) == 0
        )

    def update(self, enviroment: Enviroment):
        # first update robots
        for obj in enviroment.objects:
            if issubclass(type(obj), BaseRobot):
                cast(BaseRobot, obj).update(enviroment)
            if type(obj) is BaseRobot:
                obj.update(enviroment)

        # update babiess
        for obj in enviroment.objects:
            if issubclass(type(obj), BaseBaby):
                cast(BaseBaby, obj).update(enviroment)

        # self.print_grid(enviroment)
        # input()

    def print_grid(self, enviroment: Enviroment):
        result = ""
        v_numbers = (
            "    "
            + "".join([str(i) + ("" if i > 9 else " ") for i in range(self.width)])
            + "\n"
        )
        result += v_numbers

        for y in range(self.height):
            result += (" " if y > 9 else "  ") + str(y) + " "
            for x in range(self.width):
                objs = enviroment.find_at(Position(x, y))
                if not objs:
                    result += "."
                for obj in objs:
                    result += (
                        "R"
                        if issubclass(type(obj), BaseRobot)
                        else "B"
                        if issubclass(type(obj), BaseBaby)
                        else "O"
                        if issubclass(type(obj), Obstacle)
                        else "C"
                        if issubclass(type(obj), Corral)
                        else "_"
                        if issubclass(type(obj), Dirt)
                        else ""
                    )

                result += " "
            result += str(y) + "\n"

        result += v_numbers
        print(result)
