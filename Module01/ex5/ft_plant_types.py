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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 colour: str) -> None:
        super().__init__(name, height, age)
        self._colour = colour.lower()

    def bloom(self) -> str:
        return f"[asking {self._name.lower()} to bloom]\n" \
            f"{self.show()} \n" \
            f"{self._name} is blooming beautifully !"

    def show(self) -> str:
        return f"{super().show()}\n Color: {self._colour}"


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        return f"[asking {self._name.lower()} to produce shade]\n" \
               f"Tree {self._name} now produces a shade of " \
               f"{round(self._height, 1)} long " \
               f"and {round(self._trunk_diameter, 1)}cm wide."

    def show(self) -> str:
        return f"{super().show()} \n Trunk diameter: " \
               f"{str(self._trunk_diameter)}cm"


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_ssn: str) -> None:
        super().__init__(name, height, age)
        self._harvest_ssn = harvest_ssn.capitalize()
        self._nutr_value: int = 0

    def incr_nutr_val(self, speed: float, time: int) -> str:
        super().grow(speed)
        for i in range(0, time):
            super().age()
        self._nutr_value += time
        return f"[make {self._name.lower()} grow and age for " \
               f"{time} days]\n" \
               f"{self.show()}"

    def show(self) -> str:
        return f"{super().show()} \n Harvest Season: {self._harvest_ssn}\n "\
                f"Nutritional value: {str(self._nutr_value)}"


p1 = Flower("rose", 15.0, 10, "red")
p2 = Tree("oak", 200.0, 365, 5.0)
p3 = Vegetable("tomato", 5.0, 10, "april")

if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    print(p1.show())
    print("Rose has not bloomed yet")
    print(p1.bloom())

    print("\n=== Tree")
    print(p2.show())
    print(p2.produce_shade())

    print("\n=== Vegetable")
    print(p3.show())
    print(p3.incr_nutr_val(52.5, 20))
