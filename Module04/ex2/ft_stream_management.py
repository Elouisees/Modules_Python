#!/usr/bin/env python3

import sys
import typing


def display_file(file_name: str) -> None:
    file: typing.TextIO = open(file_name, "r")

    print("---\n")
    print(file.read())
    print("\n---")
    file.close()
    print(f"File '{file_name}' closed.\n")


def transform_file(file_name: str) -> None:
    new_content: str = ""
    new_file_name: str = ""
    file: typing.TextIO = open(file_name, "r")
    new_file: typing.TextIO = open("/dev/null", "w")

    print("Transform data: ")
    print("---\n")
    for line in file:
        if line.endswith("\n"):
            new_content += line.rstrip("\n") + "#" + "\n"
        else:
            new_content += line + "#"
    print(new_content)
    print("\n---")
    print("Enter new file name (or leave empty):")
    new_file_name = sys.stdin.readline()

    if new_file_name.strip() != "":
        print(f"Saving data to '{new_file_name.strip()}'")
        new_file = open(new_file_name, "w")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{new_file_name.strip()}'.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Acessing file '{sys.argv[1]}'")
        try:
            display_file(sys.argv[1])
            transform_file(sys.argv[1])
        except FileNotFoundError as e:
            print(e, file=sys.stderr)
        except PermissionError as e:
            print(e, file=sys.stderr)
        except OSError as e:
            print(e, file=sys.stderr)
        except Exception as e:
            print(e, file=sys.stderr)

# Notes:

# close the file to reduce the risk of it being unwarrantedly
# modified or read.
