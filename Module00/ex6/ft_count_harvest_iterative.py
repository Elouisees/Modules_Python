
def ft_count_harvest_iterative() -> None:
    print("Please enter the days untill harvest.")
    count = input("Days untill harvest: ")
    for i in range(1, int(count) + 1):
        print("Day ", i)
    print("Time to harvest!")
