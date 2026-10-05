#!/usr/bin/env python3

from typing import Callable


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant_name: str) -> None:
        super().__init__(f"The {plant_name} is wilting!")


class WaterError(GardenError):
    def __init__(self, plant_name: str) -> None:
        super().__init__(f"Not enough water in the tank for the {plant_name}")


def days_since_watered(days: int, plant_name: str) -> None:
    if days > 3:
        raise PlantError(plant_name)
    else:
        print(f"The {plant_name} has been watered enough.")


def tank_contents(liter: int, plant_name: str) -> None:
    if liter < 3:
        raise WaterError(plant_name)
    else:
        print("The tank is full of water.")


def childclass_test(func: Callable[[int, str], None],
                    nb: int, plant_name: str) -> None:
    try:
        func(nb, plant_name)
    except Exception as e:
        print(f"Caught {e.__class__.__name__}: ", e)


def parentclass_test(func: Callable[[int, str], None],
                     nb: int, plant_name: str) -> None:
    try:
        func(nb, plant_name)
    except GardenError as e:
        print(f"Caught {e.__class__.__bases__[0].__name__}: ", e)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    childclass_test(days_since_watered, 4, "tomato plant")

    print("\nTesting WaterError...")
    childclass_test(tank_contents, 1, "tomato plant")

    print("\nTesting catching all garden errors...")
    parentclass_test(days_since_watered, 4, "tomato plant")
    parentclass_test(tank_contents, 1, "tomato plant")

    print("\nAll custom error types work correctly")


# Notes

# Custom exceptions allow you to define application-specific errors
# that are not covered by the built-in exceptions

# different ways to get name of class of an instance:
# __name__ is a special variable that evaluates the name of the current
# module and can be used to print the name of a class
# type(class).__name__

# the __base__ attribute is a tuple that containts the base classes
# from which the current class inherits.

# Callable is any object that can be invoked with parantheses,
# i.e. function, classes, methods, class instances
