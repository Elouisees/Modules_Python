
from abc import ABC, abstractmethod
from ex0.battle_object import Creature, CreatureFactory


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self._name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self._name.capitalize()} uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"{self._name.capitalize()} heals {target} for a large amount"


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> "Sproutling":
        return Sproutling("sproutling", "Grass")

    def create_evolved(self) -> "Bloomelle":
        return Bloomelle("bloomelle", "Grass/Fairy")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self._state: int = 0

    def attack(self) -> str:
        att: str = ""
        if self._state == 0:
            att = "attacks normally"
        if self._state == 1:
            att = "performs a booster strike"
        return f"{self._name.capitalize()} {att}"

    def transform(self) -> str:
        self._state = 1
        return f"{self._name.capitalize()} shifts into a sharper form!" \


    def revert(self) -> str:
        self._state = 0
        return f"{self._name.capitalize()} returns to normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self._state: int = 0

    def attack(self) -> str:
        att: str = ""
        if self._state == 0:
            att = "attacks normally"
        if self._state == 1:
            att = "unleahses a devastating morph strike!"
        return f"{self._name.capitalize()} {att}"

    def transform(self) -> str:
        self._state = 1
        return f"{self._name.capitalize()} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._state = 0
        return f"{self._name.capitalize()} stabilizes its form"


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> "Shiftling":
        return Shiftling("shiftling", "Normal")

    def create_evolved(self) -> "Morphagon":
        return Morphagon("morphagon", "Normal/Dragon")
