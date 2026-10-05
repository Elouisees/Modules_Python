#!/usr/bin/env python3

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", alchemy.create_air())

    print("\nShowing that not all functions can't be reached:")
    print("Testing create_earth:", alchemy.create_earth())
