#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant_name: str) -> None:
        super().__init__(f"The {plant_name} is wilting!")


class WaterError(GardenError):
    def __init__(self, plant_name: str) -> None:
        super().__init__(f"Not enough water in the tank for the {plant_name}")


def water_plant(plant_name: str) -> None:
    if plant_name[0].isupper():
        print(f"{plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system() -> None:
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Sunflower")
        water_plant("Carrots")
    except Exception as e:
        print(f"Caught {e.__class__.__name__}: {e}\n"
              f"... ending tests and returning to main")
    finally:
        print("Closing watering system")


def test_watering_system_inv() -> None:
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("sunflower")
        water_plant("carrots")
    except Exception as e:
        print(f"Caught {e.__class__.__name__}: {e}\n"
              f"... ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system()
    print("\nTesting invalid plants")
    test_watering_system_inv()
    print("\nCleanup always happens, even with errors!")
