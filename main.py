from src.baby import Baby
from src.robot import GoalRobot, ReactiveRobot, Robot
from src.simulation import Simulation


def count(predicade, ls) -> int:
    return len(list(filter(predicade, ls)))


def print_simulation(simulations: "list[Simulation]"):
    print("RESULTS")
    total = len(simulations)
    print(f"wins: {count(lambda s: s.victory, simulations)}/{total}")
    print(f"fails: {count(lambda s: s.fail, simulations)}/{total}")

    total = 0
    for s in simulations:
        sub_total = 0
        for p in s.percents:
            sub_total += p
        sub_total /= len(s.percents)
        total += sub_total
    total /= len(simulations)
    print(f"percents: {total}")


simulations = []

simulations = [
    Simulation(
        t=30,
        total_time=100,
        width=10,
        height=10,
        obstacle_percent=15,
        dirty_percent=20,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p),
        baby_count=3,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]


for s in simulations:
    s.start_simulation()

print_simulation(simulations)
