#!/usr/bin/env python3

from ex0.battle_object import Creature, FlameFactory, AquaFactory
from ex1.capacitor_object import HealingCreatureFactory
from ex1.capacitor_object import TransformCreatureFactory
from .tournament_object import BattleStrategy, NormalStrategy
from .tournament_object import DefensiveStrategy, AgressiveStrategy


def tournament(lst_opp: list[tuple[Creature, BattleStrategy]]) -> None:
    lst_displ: list[str] = []
    displ: str = ""
    n: int = 0

    if len(lst_opp) != 0:
        for i in lst_opp:
            displ = f"({i[0].__class__.__name__}+{i[1].title})"
            lst_displ.append(displ)
        print(lst_displ)

        print("*** Tournament ***")
        print(len(lst_displ), "opponents involved")

        while n < len(lst_opp):
            m: int = n + 1
            if n == len(lst_opp) - 1:
                m = 0
            if n == 1 and len(lst_opp) == 2:
                break
            print("\n* Battle *")
            print(lst_opp[n][0].describe())
            print(" vs.")
            print(lst_opp[m][0].describe())
            print(" now fight!")
            lst_opp[n][1].act()
            lst_opp[m][1].act()
            n += 1
    else:
        raise Exception("Input error: empty list provided")


if __name__ == "__main__":
    # Creatures
    flameling = FlameFactory().create_base()
    pyrodon = FlameFactory().create_evolved()

    aquabub = AquaFactory().create_base()
    torragon = AquaFactory().create_evolved()

    sproutling = HealingCreatureFactory().create_base()  # Healing
    bloomelle = HealingCreatureFactory().create_evolved()  # Healing

    shiftling = TransformCreatureFactory().create_base()  # Transform
    morphagon = TransformCreatureFactory().create_evolved()  # Transform

    # Tournaments
    tour0 = [(flameling, NormalStrategy(flameling)),
             (sproutling, DefensiveStrategy(sproutling))]
    tour1 = [(flameling, AgressiveStrategy(flameling)),
             (sproutling, DefensiveStrategy(sproutling))]
    tour2 = [(aquabub, NormalStrategy(aquabub)),
             (sproutling, DefensiveStrategy(sproutling)),
             (shiftling, AgressiveStrategy(shiftling))]

    print("Tournament 0 (basic)")
    try:
        tournament(tour0)
    except Exception as e:
        print(e)

    print("\nTournament 1 (error)")
    try:
        tournament(tour1)
    except Exception as e:
        print(e)

    print("\nTournament 2 (multiple)")
    try:
        tournament(tour2)
    except Exception as e:
        print(e)
