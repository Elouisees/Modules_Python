#!/usr/bin/env python3

import sys


def check_input(input: list) -> None:

    inv: dict = {}
    temp: list = []
    sign: int = 0

    for i in range(0, len(input)):
        sign = 0
        if (input[i][len(input[i]) - 2]) != ":":
            print(f"Error - invalid parameter '{input[i]}'")
        else:
            item: list = input[i].split(":")
            for x in temp:
                if x == item[0]:
                    print(f"Rendundant item '{item[0]}' - discarding")
                    sign = 1
            if sign == 1:
                continue
            if str(item[1]).isdigit() is False:
                print(f"Quantity error for '{item[0]}': invalid literal "
                      f"for int() with base 10: '{item[1]}'")
                continue

            temp.append(item[0])
            temp.append(int(item[1]))

    inv = {temp[i]: temp[i + 1]
           for i in range(0, len(temp), 2)}

    print("Got inventory: ", inv)
    print("Item list: ", list(inv.keys()))
    print(f"Total quantity of the {len(inv)} items: {sum(inv.values())}")

    mst = int(max(tuple(inv.values())))
    lst = int(min(tuple(inv.values())))

    item_mst: str = ""
    item_lst: str = ""

    for key in inv:
        if inv[key] == mst:
            item_mst = key
        if inv[key] == lst:
            item_lst = key
        print(f"Item {key} represents "
              f"{round((inv[key] / sum(inv.values())) * 100, 1)}%")

    print(f"Item most abundant: {item_mst} with quantity {mst}")
    print(f"Item least abundant: {item_lst} with quantity {lst}")

    inv.update({"magic_item": 2})
    print("Updated inventory: ", inv)


if __name__ == "__main__":

    print("=== Inventory System Analysis ===")
    try:
        if len(sys.argv) == 1:
            print("Error: no input data received")
            print("Example input data: ./name_file sword:1 potion:5")
        else:
            check_input(sys.argv[1: len(sys.argv)])
    except Exception as e:
        print(e)
