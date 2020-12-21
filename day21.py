from collections import defaultdict
from copy import copy

# cqvc vmkt sbvbzcg (contains fish, soy, nuts)

ingredients = defaultdict(set)
allergens = {}

with open("day21.in") as f:
    LINES = f.read().splitlines()

# LINES = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

for line in LINES:
    i, a = line.rstrip(")").split("(contains ")
    i = frozenset(i.split())
    a = a.split(", ")

    allergens[i] = a
    for allergen in a:
        ingredients[allergen].add(i)

# print(ingredients)
# print(allergens)

intersected_ingredients = {}
for a, ins in ingredients.items():
    ins_copy = set(ins)

    intersection = set(ins_copy.pop())
    for s in ins_copy:
        intersection.intersection_update(s)
    
    # print(a, intersection)
    intersected_ingredients[a] = intersection

unique_ingredients = {}
while len(intersected_ingredients) > 0:
    allergen = min(intersected_ingredients, key=lambda k: len(intersected_ingredients[k]))
    ingredients = intersected_ingredients[allergen]
    n = len(intersected_ingredients[allergen])
    if n != 1:
        print("error: next allergen is not present in a single ingredient")
        break

    ingredient = ingredients.pop()
    unique_ingredients[allergen] = ingredient 

    for a, ins in intersected_ingredients.items():
        ins.discard(ingredient)
    
    del intersected_ingredients[allergen]

print(unique_ingredients)

count = 0
for ins in allergens:
    for i in ins:
        if i not in unique_ingredients.values():
            count += 1

print(count)
print(",".join([unique_ingredients[k] for k in sorted(unique_ingredients)]))
