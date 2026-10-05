#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._stats = Plant.Stats()

        if height < 0:
            print("Error, height cannot be negative.")
        else:
            self._height = height

        if age < 0:
            print("Error, age cannot be negative.")
        else:
            self._age = age

    @staticmethod
    def check_age(age: int) -> str:
        mess: str = f"Is {age} days more than a year? -> "

        if age > 365:
            mess += "True"
        else:
            mess += "False"

        return mess

    @classmethod
    def anonymous(cls):
        return cls(name="Unknown plant", height=0.0, age=0)

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

    def grow(self, speed: float) -> None:
        self._height += 0.8 * speed
        self._stats.grow_cnt()

    def age(self, time: int) -> None:
        self._age += time
        self._stats.age_cnt()

    def show(self) -> str:
        self._stats.show_cnt()
        return f"{self._name}: {str(round(self._height, 1))}cm, " \
               f"{str(self._age)} days old"

    def display_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        print(self._stats.display())

    class Stats():
        def __init__(self) -> None:
            self._growcnt: int = 0
            self._agecnt: int = 0
            self._showcnt: int = 0
            self._produce_shadecnt: int = 0

        def grow_cnt(self) -> None:
            self._growcnt += 1

        def age_cnt(self) -> None:
            self._agecnt += 1

        def show_cnt(self) -> None:
            self._showcnt += 1

        def display(self) -> str:
            return f"Stats: {self._growcnt} grow, {self._agecnt} age, " \
                    f"{self._showcnt} show"


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 colour: str) -> None:
        super().__init__(name, height, age, colour)
        self._seeds: int = 0

    def bloom(self) -> str:
        self._seeds += 42
        return super().bloom()

    def show(self) -> str:
        return f"{super().show()}\n Seeds: {self._seeds}"


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def produce_shade(self) -> str:
        self._stats._produce_shadecnt += 1
        return f"[asking {self._name.lower()} to produce shade]\n" \
               f"Tree {self._name} now produces a shade of " \
               f"{round(self._height, 1)} long " \
               f"and {round(self._trunk_diameter, 1)}cm wide."

    def show(self) -> str:
        return f"{super().show()} \n Trunk diameter: " \
                f"{str(self._trunk_diameter)}cm"

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()

        def display(self) -> str:
            return f"Stats: {self._growcnt} grow, {self._agecnt} age, " \
                    f"{self._showcnt} show, {self._produce_shadecnt} shade"


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_ssn: str) -> None:
        super().__init__(name, height, age)
        self._harvest_ssn = harvest_ssn.capitalize()
        self._nutr_value: int = 0

    def incr_nutr_val(self, speed: float, time: int) -> str:
        super().grow(speed)
        super().age(time)
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
p4 = Seed("Sunflower", 80.0, 45, "yellow")
p5 = Plant.anonymous()

if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(Plant.check_age(30))
    print(Plant.check_age(400))

    print("\n=== Flower")
    print(p1.show())
    print("Rose has not bloomed yet")
    p1.display_stats()
    print("[asking the rose to grow and bloom]")
    p1.grow(10)
    print(p1.bloom())
    p1.display_stats()

    print("\n=== Tree")
    print(p2.show())
    p2.display_stats()
    print(p2.produce_shade())
    p2.display_stats()

    print("\n=== Seed")
    print(p4.show())
    print("[make sunflower grow, age and bloom]")
    p4.grow(37.5)
    p4.age(20)
    print(p4.bloom())
    p4.display_stats()

    print("\n=== Anonymous")
    print(p5.show())
    p5.display_stats()

# Notes:

# classmethod -> a second constructor that builds a plant
# with incomplete information

# staticmethod -> a method defined within a class that does
# not depens on any instances or class data.
# It is used when a function logically belongs to a class
# but does not need access to self or cls.
