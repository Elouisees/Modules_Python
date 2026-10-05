#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments provided!")

    print("Total arguments: ", len(sys.argv))
