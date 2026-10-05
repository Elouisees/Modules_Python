#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: str, age: str) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


p1_rose = Plant("Rose", "25", "30")
p2_sunfl = Plant("Sunflower", "80", "45")
p3_cactus = Plant("Cactus", "15", "120")

if __name__ == "__main__":
    print("=== Garden PLant Registry ===")
    p1_rose.show()
    p2_sunfl.show()
    p3_cactus.show()


# Notes:

# Shebang allows to run a python SCRIPT directly, without
# explicitly typing python/python3

# the first line of a script that specifies which
# interpreter should be used to execute the script

# The **env utility** looks up the interpreter in the system's
# PATH environment variable instead of relying on a hard-coded
# location. It makes the shebang portable, environment-aware, version-safe.
