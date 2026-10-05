
def ft_harvest_total() -> None:
    print("Please enter the weight of your harvest for each day.")
    day_one = input("Day 1 harvest: ")
    day_two = input("Day 2 harvest: ")
    day_three = input("Day 3 harvest: ")
    print("Total harvest:", int(day_one) + int(day_two) + int(day_three))
