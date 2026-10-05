#!/usr/bin/env python3

import random

achievements = {
    "Stone Age", "Hot Stuff", "We Need to Go Deeper",
    "Zombie Doctor", "Adventure", "Monster Hunter",
    "Caves & Cliffs", "Hero of the Village", "Star Trader",
    "Sound of Music", "Hot Tourist Destinations", "War Pigs",
    "Spooky Scary Skeleton", "Cover Me with Diamonds", "Sky's the Limit"
    "Sweet Dreams", "Hired Help", "Who's the Pillager Now?",
    "Fishy Business", "A Seedy Place", "Birthday Song"
    }


def gen_player_achievements() -> None:

    # achievement sets
    pl1: list = random.sample(list(achievements), random.randint(5, 9))
    pl2: list = random.sample(list(achievements), random.randint(5, 9))
    pl3: list = random.sample(list(achievements), random.randint(5, 9))
    pl4: list = random.sample(list(achievements), random.randint(5, 9))

    # print

    print("Player 1 - ", set(pl1))
    print("Player 2 - ", set(pl2))
    print("Player 3 - ", set(pl3))
    print("Player 4 - ", set(pl4))

    # ------------------------------------------ DISTINCT ACHIEVEMENTS
    print("\n--- DISTINCT ACHIEVEMENTS ---")
    print("All distinct achievements: ",
          achievements.union(set(pl1), set(pl2), set(pl3), set(pl4)))

    # ------------------------------------------ COMMON ACHIEVEMENTS
    print("\n--- COMMON ACHIEVEMENTS ---")
    print("Common acievements: ",
          set(pl1).intersection(set(pl2), set(pl3), set(pl4)))

    # ------------------------------------------ UNIQUE ACHIEVEMENTS
    print("\n--- UNIQUE ACHIEVEMENTS ---")
    print("Only Player 1 has: ",
          set(pl1).difference(set(pl2), set(pl3), set(pl4)))
    print("Only Player 2 has: ",
          set(pl2).difference(set(pl3), set(pl4), set(pl1)))
    print("Only Player 3 has: ",
          set(pl3).difference(set(pl4), set(pl1), set(pl2)))
    print("Only Player 4 has: ",
          set(pl4).difference(set(pl1), set(pl2), set(pl3)))

    # ------------------------------------------ MISSING ACHIEVEMENTS
    print("--- MISSING ACHIEVEMENTS ---")
    print(f"Player 1 is missing: \n"
          f"{achievements.difference(set(pl1))}\n")
    print(f"Player 2 is missing: \n"
          f"{achievements.difference(set(pl2))}\n")
    print(f"Player 3 is missing: \n"
          f"{achievements.difference(set(pl3))}\n")
    print(f"Player 4 is missing: \n"
          f"{achievements.difference(set(pl4))}\n")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
    print("==================================")


# Notes

# Set only stores unique items, duplicates are automatically
# removed.
# No fixed positions, cant be accessed through indexing
# hashing used internally for search

# An empty set is printed as: set(),
# using '{}' would create and empty dictionary
