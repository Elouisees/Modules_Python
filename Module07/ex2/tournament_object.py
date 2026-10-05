#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):
    def __init__(self) -> None:
        self.title: str = ""

    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self, creature: Any) -> None:
        self.title: str = "Normal"
        self.creature = creature

    def act(self) -> None:
        if not self.is_valid():
            raise Exception(f"Battle error, aborting tournament: "
                            "Invalid Creature "
                            f"'{self.creature._name.capitalize()}'"
                            " for this aggresive strategy")
        print(self.creature.attack())

    def is_valid(self) -> bool:
        return callable(getattr(self.creature, "attack", None))


class AgressiveStrategy(BattleStrategy):
    def __init__(self, creature: Any) -> None:
        self.title: str = "Aggresive"
        self.creature = creature

    def act(self) -> None:
        if not self.is_valid():
            raise Exception(f"Battle error, aborting tournament: "
                            "Invalid Creature "
                            f"'{self.creature._name.capitalize()}'"
                            " for this aggresive strategy")
        print(self.creature.transform())
        print(self.creature.attack())
        print(self.creature.revert())

    def is_valid(self) -> bool:
        return callable(getattr(self.creature, "transform", None))


class DefensiveStrategy(BattleStrategy):
    def __init__(self, creature: Any) -> None:
        self.title = "Defensive"
        self.creature = creature

    def act(self) -> None:
        if not self.is_valid():
            raise Exception(f"Battle error, aborting tournament: "
                            "Invalid Creature "
                            f"'{self.creature._name.capitalize()}'"
                            " for this aggresive strategy")
        print(self.creature.attack())
        print(self.creature.heal("itself"))

    def is_valid(self) -> bool:
        return callable(getattr(self.creature, "heal", None))
