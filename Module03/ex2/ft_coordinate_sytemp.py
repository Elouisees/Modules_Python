#!/usr/bin/env python3

import math


def get_player_pos() -> tuple:

    s_one: list = [float]
    s_two: list = [float]

    print("Get a first set of coordinates")
    while True:
        # first set coordinates
        x = input()
        print("Enter new coordinates as floats in format 'x.x,y.y,z.z': ", x)

        try:
            coords = x.split(",", 2)
            if len(coords) < 3:
                raise ValueError
            for i in range(0, 3):
                s_one.append(round(float(coords[i]), 1))
        except Exception:
            print("Invalid syntax")
            continue

        dis: float = round(math.sqrt((0 - s_one[0]) ** 2 +
                                     (0 - s_one[1]) ** 2 +
                                     (0 - s_one[2]) ** 2), 4)

        print(f"It includes: X={s_one[0]}, Y={s_one[1]}, "
              f"Z={s_one[2]}")
        print("Distance to center: ", dis)

        print("\nGet a second set of coordinates")
        while True:
            # second set coordinates
            x = input()
            print("Enter new coordinates as floats in format 'x,y,z': ", x)

            try:
                coords = x.split(",", 2)
                if len(coords) < 3:
                    raise ValueError
                for i in range(0, 3):
                    s_two.append(round(float(coords[i]), 1))
            except Exception as e:
                print(f"Error on parameter '{coords[i]}': ", e)
                continue

            dis_two: float = round(math.sqrt((s_two[0] - s_one[0]) ** 2 +
                                             (s_two[1] - s_one[1]) ** 2 +
                                             (s_two[2] - s_one[2]) ** 2), 4)

            print("Distance between the 2 sets of coordinates: ", dis_two)
            return (tuple(s_two))


if __name__ == "__main__":
    print("=== Game Coordinate Sytem ===\n")
    try:
        get_player_pos()
    except Exception as e:
        print(e)
