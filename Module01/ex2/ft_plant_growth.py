#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self.height = height
        self._age = age

    def grow(self, speed: float) -> None:
        self.height += 0.8 * speed

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {str(round(self.height, 1))}cm, "
              f"{str(self._age)} days old")


p1_rose = Plant("Rose", 25.0, 30)

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    p1_rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1_rose.grow(1)
        p1_rose.age()
        p1_rose.show()
    print(f"Growth this week: {round(p1_rose.height - 25, 1)}cm")


# Notes:

# 'self' is a name for the firts parameter of methods in classes,
# representing the instance of the classes itself.

# it allows access to instance attributes/methods, differentiating between
# instance variables and local/global variables.
