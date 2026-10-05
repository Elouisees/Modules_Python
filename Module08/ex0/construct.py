#!/usr/bin/env python3

import os
import sys
import site

if __name__ == "__main__":
    if 'VIRTUAL_ENV' in os.environ:
        print("MATRIX STATUS: Welcome to the construct")

        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment: matrix_venv")
        print("Environment Path:", sys.prefix)

        print("\nSUCCESS: You're in the isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("Package installation path:")
        print(site.getusersitepackages())

        print("\nThen run this program again")
    else:
        print("MATRIX STATUS: You're still plugged in")

        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment: None detected")\

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print(" python -m venv <ve_name>")
        print(" source ve_name/bin/activate # On Linux")
        print(" ve_name\\Scripts\activate    # On Windows")

        print("\nThen run this program again")
