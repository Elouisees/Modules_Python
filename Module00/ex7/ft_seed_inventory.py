
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    x = unit
    if unit == "grams":
        x = unit + " total"
        print(seed_type.capitalize(), "seeds: ", str(quantity), x)
    elif unit == "area":
        x = "square meters"
        print(seed_type.capitalize(), "seeds: covers", str(quantity), x)
    elif unit == "unknown":
        print("Unknown unit type")
    else:
        x = unit + " available"
        print(seed_type.capitalize(), "seeds: ", str(quantity), x)
