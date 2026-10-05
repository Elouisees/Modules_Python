#!/usr/bin/env python3

import random

names_players: list[str] = ["Ella", "kevin", "Bob", "Arthur",
                            "jaiylin", "Fiona", "abel", "Kaine",
                            "ruth", "Quincy", "Carl", "dorothea"]


def order_data(names: list[str]) -> None:
    lst_cap: list[str] = []
    lst_all_cap: list[str] = []
    scores: dict = {}
    high_scr: dict = {}
    average: float = 0

    for name in names:
        if name[0].isupper():
            lst_cap += [name]
        lst_all_cap += [name.capitalize()]

    scores = {name: random.randint(250, 1000) for name in lst_all_cap}
    average = round(sum(scores.values()) / len(scores), 2)
    for k in scores:
        if scores[k] >= average:
            high_scr[k] = scores[k]

    print("\nNew list with all names capitalized: ", lst_all_cap)
    print("\nNew list of capitalized names only: ", lst_cap)
    print("\nScore dict: ", scores)
    print("Score average is", average)
    print("High scores: ", high_scr)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print("Initial list of players: ", names_players)
    order_data(names_players)
