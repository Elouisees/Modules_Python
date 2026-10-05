
def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    try:
        new_str: list[str] | str = ingredients.split(" ")
    except Exception:
        new_str = ingredients

    test: list[str] = []
    new_comp: list[str] = []

    for elem in new_str:
        if elem == "and" or elem == "+" or elem == "&":
            continue
        if elem[len(elem) - 1] == ",":
            elem = elem[:-1]
            test.append(elem)
        else:
            test.append(elem)

    for elem in light_spell_allowed_ingredients():
        new_comp.append(elem.capitalize())

    count: int = 0
    for item in test:
        if item.capitalize() in new_comp:
            count += 1
    if count == 0:
        return f"({ingredients} - INVALID)"
    return f"({ingredients}) - VALID"
