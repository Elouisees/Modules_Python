#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(input: str) -> None:
    print(f"Input data is '{input}'")
    try:
        print(f"Temperature is now {input_temperature(input)}°C\n")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    test_temperature("abc")
    print("\nAll tests completed - program didn't crash!")
