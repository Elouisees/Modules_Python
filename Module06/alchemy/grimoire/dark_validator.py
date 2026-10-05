
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

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

    for elem in dark_spell_allowed_ingredients():
        new_comp.append(elem.capitalize())

    for item in test:
        if item.capitalize() not in new_comp:
            return f"({ingredients} - INVALID)"
    return f"({ingredients}) - VALID"
