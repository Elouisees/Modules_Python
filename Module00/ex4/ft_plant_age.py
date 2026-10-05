
def ft_plant_age() -> None:
    plant_age = input("Enter plant age in days: ")
    if int(plant_age) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant is not ready to harvest, yet!")
