from src.baby import Baby
from src.robot import GoalRobot, ReactiveRobot, Robot
from src.simulation import Simulation

handler = open("results.txt", mode="w+")


def count(predicade, ls) -> int:
    return len(list(filter(predicade, ls)))


def print_simulation(simulations: "list[Simulation]", name: str):
    print("RESULTS")
    total = len(simulations)
    wins = f"wins: {count(lambda s: s.victory, simulations)}/{total}"
    fails = f"fails: {count(lambda s: s.fail, simulations)}/{total}"
    total = 0
    for s in simulations:
        sub_total = 0
        for p in s.percents:
            sub_total += p
        sub_total /= len(s.percents)
        total += sub_total
    total /= len(simulations)
    percents = f"percents: {total}"

    lines = [name, wins, fails, percents]
    handler.write(" \n".join(lines) + "\n\n")
    handler.flush()
    print(lines)


simulations = []

simulationsS1R = [
    Simulation(
        t=15,
        total_time=100,
        width=10,
        height=10,
        obstacle_percent=10,
        dirty_percent=10,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=4,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS2R = [
    Simulation(
        t=15,
        total_time=100,
        width=10,
        height=10,
        obstacle_percent=20,
        dirty_percent=10,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=4,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS3R = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=10,
        dirty_percent=20,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=4,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS4R = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=30,
        dirty_percent=5,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=5,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS5R = [
    Simulation(
        t=15,
        total_time=100,
        width=30,
        height=30,
        obstacle_percent=20,
        dirty_percent=0,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=6,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS6R = [
    Simulation(
        t=15,
        total_time=100,
        width=20,
        height=20,
        obstacle_percent=10,
        dirty_percent=10,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=5,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS7R = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=10,
        dirty_percent=40,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=2,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS8R = [
    Simulation(
        t=15,
        total_time=100,
        width=20,
        height=20,
        obstacle_percent=5,
        dirty_percent=0,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=10,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS9R = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=25,
        dirty_percent=40,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=1,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS10R = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=0,
        dirty_percent=0,
        robot_count=1,
        robot_factory=lambda p: ReactiveRobot(p),
        baby_count=5,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]


simulationsS1C = [
    Simulation(
        t=15,
        total_time=100,
        width=10,
        height=10,
        obstacle_percent=10,
        dirty_percent=10,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=4,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS2C = [
    Simulation(
        t=15,
        total_time=100,
        width=10,
        height=10,
        obstacle_percent=20,
        dirty_percent=10,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=4,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS3C = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=10,
        dirty_percent=20,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=4,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS4C = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=30,
        dirty_percent=5,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=5,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS5C = [
    Simulation(
        t=15,
        total_time=100,
        width=30,
        height=30,
        obstacle_percent=20,
        dirty_percent=0,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=6,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS6C = [
    Simulation(
        t=15,
        total_time=100,
        width=20,
        height=20,
        obstacle_percent=10,
        dirty_percent=10,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=5,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS7C = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=10,
        dirty_percent=40,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=2,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS8C = [
    Simulation(
        t=15,
        total_time=100,
        width=20,
        height=20,
        obstacle_percent=5,
        dirty_percent=0,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=10,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS9C = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=25,
        dirty_percent=40,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=1,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]

simulationsS10C = [
    Simulation(
        t=15,
        total_time=100,
        width=15,
        height=15,
        obstacle_percent=0,
        dirty_percent=0,
        robot_count=1,
        robot_factory=lambda p: GoalRobot(p, 30),
        baby_count=5,
        baby_factory=lambda p: Baby(p),
    )
    for _ in range(30)
]


def process_simulations(simulations, name: str):
    for s, i in zip(simulations, range(len(simulations))):
        s.start_simulation()
        print(f"{i+1}/{len(simulations)-1}")
    print_simulation(simulations, name)


print("RS1:")
process_simulations(simulationsS1R, "RS1")
print("RS2:")
process_simulations(simulationsS2R, "RS2")
print("RS3:")
process_simulations(simulationsS3R, "RS3")
print("RS4:")
process_simulations(simulationsS4R, "RS4")
print("RS5:")
process_simulations(simulationsS5R, "RS5")
print("RS6:")
process_simulations(simulationsS6R, "RS6")
print("RS7:")
process_simulations(simulationsS7R, "RS7")
print("RS8:")
process_simulations(simulationsS8R, "RS8")
print("RS9:")
process_simulations(simulationsS9R, "RS9")
print("RS10:")
process_simulations(simulationsS10R, "RS10")

print("CS1:")
process_simulations(simulationsS1C, "CS1")
print("CS2:")
process_simulations(simulationsS2C, "CS2")
print("CS3:")
process_simulations(simulationsS3C, "CS3")
print("CS4:")
process_simulations(simulationsS4C, "CS4")
print("CS5:")
process_simulations(simulationsS5C, "CS5")
print("CS6:")
process_simulations(simulationsS6C, "CS6")
print("CS7:")
process_simulations(simulationsS7C, "CS7")
print("CS8:")
process_simulations(simulationsS8C, "CS8")
print("CS9:")
process_simulations(simulationsS9C, "CS9")
print("CS10:")
process_simulations(simulationsS10C, "CS10")
