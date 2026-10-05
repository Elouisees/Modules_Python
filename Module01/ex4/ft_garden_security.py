#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        if height < 0:
            print("Error, height cannot be negative.")
        else:
            self._height = height

        if age < 0:
            print("Error, age cannot be negative.")
        else:
            self._age = age

    def grow(self, speed: float) -> None:
        self._height += 0.8 * speed

    def age(self) -> None:
        self._age += 1

    def set_height(self, new_height) -> str:
        if new_height < 0:
            return f"{self._name}: Error, height cannot be negative\n" \
                    f"Height update rejected"
        else:
            self._height = new_height
            return f"Height updated: {str(self._height)}cm"

    def set_age(self, new_age) -> str:
        if new_age < 0:
            return f"{self._name}: Error, age cannot be negative\n" \
                    f"Age update rejected"
        else:
            self._age = new_age
            return f"Age updated: {str(self._age)} days"

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> str:
        return f"{self._name}: {str(round(self._height, 1))}cm, " \
              f"{str(self._age)} days old"


p1 = Plant("rose", 15.0, 10)

if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Plant created: ", p1.show())
    print("\n")

    print(p1.set_height(25))
    print(p1.set_age(30))
    print("\n")

    print(p1.set_height(-25))
    print(p1.set_age(-30))
    print("\n")

    print("Current state:", p1.show())
