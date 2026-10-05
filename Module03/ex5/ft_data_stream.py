#!/usr/bin/env python3

import random

from typing import Generator

players: list = ["Arne", "Benedict", "Cassian", "Drogo",
                 "Emil", "Godwin", "Maurin", "Njal",
                 "Amelia", "Bogdana", "Cicilia", "Dorothy",
                 "Ella", "Mirabel", "Petra"]

actions: list = ["walk", "run", "sit", "eat", "sleep",
                 "jump", "swim", "fight", "open", "close",
                 "move", "crouch", "grab", "hunt", "fish",
                 "gather", "talk", "hide"]


def gen_event() -> Generator[tuple, None, None]:

    while True:
        action: str = actions[random.randint(0, 17)]
        player: str = players[random.randint(0, 14)]

        combo: tuple = (player, action)
        yield combo


def consume_event(lst_crtd: list) -> Generator[list[tuple], None, None]:

    while True:

        index = random.randint(0, len(lst_crtd) - 1)
        print("\nGot event from list: ", lst_crtd[index])
        del lst_crtd[index]
        print("Remains in list: ", lst_crtd)
        yield lst_crtd


if __name__ == "__main__":
    my_gen: Generator = gen_event()
    combo_main: tuple = ()
    lst_gen: list[tuple] = []

    print("=== Game Data Stream Processor ===")
    for i in range(0, 1000):
        combo_main = next(my_gen)
        print(f"Event {i}: Player {combo_main[0]} did action {combo_main[1]}")

    for i in range(10):
        lst_gen.append(next(my_gen))

    print("\nBuilt list of 10 events: ", lst_gen)
    change = consume_event(lst_gen)
    for i in range(0, 10):
        next(change)
