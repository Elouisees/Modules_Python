
from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self._name = name
        self._type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name.capitalize()} is a "\
               f"{self._type.capitalize()} type Creature"


class Flameling(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> "Creature":
        pass

    @abstractmethod
    def create_evolved(self) -> "Creature":
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> "Flameling":
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> "Pyrodon":
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):

    def create_base(self) -> "Aquabub":
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> "Torragon":
        return Torragon("Torragon", "Water")
