
def ft_count_harvest_recursive() -> None:
    print("Please enter the days untill harvest.")
    days = input("Days untill harvest: ")

    def count_up(current, days) -> int:
        if current > days:
            return
        else:
            print("Day ", int(current))
            count_up(current + 1, days)
    count_up(1, int(days))
    print("Time to harvest!")
