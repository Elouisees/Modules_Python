#!/usr/bin/env python3

import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Acessing file '{sys.argv[1]}'")
        try:
            file: typing.TextIO = open(sys.argv[1])
            print("---\n")
            print(file.read())
            print("\n---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
        except FileNotFoundError as e:
            print(e)
        except PermissionError as e:
            print(e)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)

# Notes:

# close the file to reduce the risk of it being unwarrantedly
# modified or read.
