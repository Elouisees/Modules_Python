#!/usr/bin/env python3

from .battle_object import CreatureFactory, FlameFactory, AquaFactory


def check_objs(creature: "CreatureFactory") -> None:
    print("\nTesting Factory")
    try:
        if creature.create_base() and creature.create_evolved():
            # Flameling
            print(creature.create_base().describe())
            print(creature.create_base().attack())

            # Pyrodon
            print(creature.create_evolved().describe())
            print(creature.create_evolved().attack())
        else:
            raise ValueError
    except Exception:
        print("Creature could not be created.")


def creature_fight(cr_one: "FlameFactory", cr_two: "AquaFactory") -> None:
    print("\nTesting Battle")
    print(cr_one.create_base().describe())
    print(" vs.")
    print(cr_two.create_base().describe())
    print(" fight!")
    print(cr_one.create_base().attack())
    print(cr_two.create_base().attack())


if __name__ == "__main__":
    fire_cr: "FlameFactory" = FlameFactory()
    water_cr: "AquaFactory" = AquaFactory()

    check_objs(fire_cr)
    check_objs(water_cr)
    creature_fight(fire_cr, water_cr)
