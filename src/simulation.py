from typing import Callable

from .agent import Baby, Robot
from .enviroment import Enviroment
from .object import Corral, Dirt, Obstacle  # noqa: F401
from .util import Position, get_random_position


class Simulation:
    def __init__(
        self,
        time: int,
        total_time: int,
        width: int,
        height: int,
        obstacle_percent: int,
        dirty_percent: int,
        robot_count: int,
        robot_factory: "Callable[[Position],Robot]",
        baby_count: int,
        baby_factory: "Callable[[Position],Baby]",
    ):
        self.time = time
        self.total_time = total_time
        self.width = width
        self.height = height

        self.obstacle_percent = obstacle_percent
        self.dirty_percent = dirty_percent

        self.robot_count = robot_count
        self.robot_factory = robot_factory

        self.baby_count = baby_count
        self.baby_factory = baby_factory

    def __generate_enviroment(self):
        self.enviroment: Enviroment = Enviroment(self.width, self.height)

        positions = list(
            get_random_position(self.width, self.height)
        )  # All avalidable positions

        for _ in range(self.robot_count):
            robot = self.robot_factory(positions.pop())
            self.enviroment.objects.append(robot)

        for _ in range(self.baby_count):
            baby = self.baby_factory(positions.pop())
            self.enviroment.objects.append(baby)

        total = self.width * self.height
        for _ in range(self.dirty_percent * total // 100):
            if positions:
                self.enviroment.objects.append(Dirt(positions.pop()))

        for _ in range(self.obstacle_percent * total // 100):
            if positions:
                self.enviroment.objects.append(Obstacle(positions.pop()))

    def start_simulation(self):
        self.__generate_enviroment()
        for i in range(self.total_time):
            for j in range(self.time):
                self.update(self.enviroment)
                # TODO: check end condition
            print(f"Iteration: {i}")
            self.__generate_enviroment()

    def update(self, enviroment: Enviroment):
        # first update robots
        for obj in enviroment.objects:
            if type(obj) is Robot:
                obj.update(enviroment)
        # update babies
        for obj in enviroment.objects:
            if type(obj) is Baby:
                obj.update(enviroment)
