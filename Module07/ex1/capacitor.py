#!/usr/bin/env python3

from .capacitor_object import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    sproutling = HealingCreatureFactory().create_base()
    bloomelle = HealingCreatureFactory().create_evolved()

    shiftling = TransformCreatureFactory().create_base()
    morphagon = TransformCreatureFactory().create_evolved()

    print("Testing Creature with healing capability\n   base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal("itself"))
    print(" evolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal("itself and others"))

    print("\nTesting Creature with transform capability\n   base:")
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())
    print(" evolved:")
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())

# run outside package as: python3 -m ex1.capacitor
