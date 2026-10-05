#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    if temp_str[0] == "-" or temp_str[0] == "+":
        if temp_str[1:len(temp_str)].isdigit() is False:
            raise ValueError
    elif temp_str.isdigit() is False:
        raise ValueError("Temperature can only contain numeric characters.\n")

    if int(temp_str) > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C).\n")
    if int(temp_str) < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C).\n")

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
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didnt crash!")
