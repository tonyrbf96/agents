from src.babies import ReactiveBaby
from src.robots import ReactiveRobot
from src.simulation import Simulation

simulation = Simulation(
    30, 100, 30, 30, 10, 20, 1, lambda p: ReactiveRobot(p), 1, lambda p: ReactiveBaby(p)
)

simulation.start_simulation()

print(simulation.enviroment)
