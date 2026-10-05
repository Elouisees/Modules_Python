#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:  # ValueError
        int("abc")
    elif operation_number == 1:  # ZeroDivisionError
        10 / 0
    elif operation_number == 2:  # FileNotFoundError
        open("abc.txt")
    elif operation_number == 3:  # TypeError
        "abc" + 25
    else:
        return


def test_error_types(input: int) -> None:
    print(f"Testing operation {input}...")
    try:
        garden_operations(input)
        print("Operation completed successfully")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        test_error_types(i)
    print("\nAll error types tested successfully!")


# Notes

# ValueError: occurs when function receives an argument
# of the correct data type, but with an invalid value.
# Python understands the type of the value provided, but
# the value itself is not suitable for the operations being performed.

# ZeroDivisionError: occurs when there is an attempt to
# divide a number by 0.
# Division by 0 is mathematically undefined, therefore stops
# Python the program and raises an exception

# FileNotFoundError: occurs when trying to access a file that does
# not exist *at the specified location)

# TypeError: occurs when an operation is applied to an
# object of an innapropriate type
