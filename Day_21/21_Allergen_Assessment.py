import fileinput


class Food:
    ingredients: set[str]
    allergens: set[str]

    def __init__(self, ingredients: set[str], allergens: set[str]):
        self.ingredients = ingredients
        self.allergens = allergens

    def __repr__(self):
        return f"Food: {self.ingredients}, {self.allergens}"

    def __str__(self):
        return self.__repr__()


def main() -> None:
    foods: list[Food] = []

    all_allergens: set[str] = set()
    all_ingredients: set[str] = set()

    line: str
    for line in [
        line.rstrip().replace("(", "").replace(",", "").replace(")", "") for line in fileinput.input() if line != "\n"
    ]:
        halves: list[str] = line.split(" contains ")
        ingredients: set[str] = set(halves[0].split(" "))
        allergens: set[str] = set(halves[1].split(" "))
        del halves

        foods.append(Food(ingredients, allergens))
        all_allergens |= allergens
        all_ingredients |= ingredients
        del ingredients, allergens
    del line

    possible: dict[str, set[str]] = {}
    for allergen in all_allergens:
        food_ings: list[set[str]] = [f.ingredients for f in foods if allergen in f.allergens]
        possible[allergen] = food_ings[0].intersection(*food_ings[1:])

    impossible = all_ingredients.difference(*possible.values())
    print(
        "Part 1:",
        sum([len(food.ingredients.intersection(impossible)) for food in foods]),
    )

    definite: dict[str, str] = {}

    last = -1
    while last != len(possible):
        last = len(possible)
        for ing in [ing for ing in possible if len(possible[ing]) == 1]:
            allergen = possible[ing].pop()
            definite[ing] = allergen
            del possible[ing]

            for i in possible.values():
                i.discard(allergen)

    print("Part 2:", ",".join([definite[k] for k in sorted(definite.keys())]))


if __name__ == "__main__":
    main()
