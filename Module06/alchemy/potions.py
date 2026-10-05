
from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}'"\
            f"and '{create_air()}'"
# import function from module in current dir


def strength_potion() -> str:
    return f"Strength potion brewed with '{create_fire()}'"\
           f"and '{create_water()}'"
# import functions from module in parent dir (relative)


heal = healing_potion
