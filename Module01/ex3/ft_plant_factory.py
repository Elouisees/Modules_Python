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

    def show(self) -> str:
        return f"{self._name}: {str(round(self.height, 1))}cm, " \
              f"{str(self._age)} days old"


p1 = Plant("Rose", 25.0, 30)
p2 = Plant("Sunflower", 80, 45)
p3 = Plant("Cactus", 15, 120)
p4 = Plant("Oak", 200.0, 365)
p5 = Plant("fern", 15.0, 120)

plant_lst: list = [p1, p2, p3, p4, p5]

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    for plant in plant_lst:
        print("Created:", plant.show())
