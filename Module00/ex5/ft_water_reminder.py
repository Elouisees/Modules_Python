
def ft_water_reminder() -> None:
    print("Please enter the number of days since the last watering.")
    water_history = input("Days since last watering: ")
    if int(water_history) > 2:
        print("Water the plants!")
    else:
        print("The plants are fine.")
