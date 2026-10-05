
# . -> current package, .. -> parent package, ... -> grandparent package
# (only works if every directory above the file has an __init__.py)
# can only climb inside the package
from ..elements import create_air

from elements import create_fire
from alchemy.potions import strength_potion  # absolute path


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: '{create_air()}' and"\
        f"'{strength_potion()}' mixed with '{create_fire()}'"
