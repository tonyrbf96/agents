from .enviroment import Enviroment
from .object import Corral, Dirt
from .obstacle import Obstacle


def calculate_dirty(enviroment: Enviroment):
    return (
        len(enviroment.search_by_type([Dirt]))
        * 100
        // (
            enviroment.width * enviroment.height
            - len(enviroment.search_by_type([Obstacle]))
            - len(enviroment.search_by_type([Corral]))
        )
    )
