from collections import namedtuple

Inclusion = namedtuple("Inclusion", "num col")

contains = {}
contained_by = {}

# clear teal bags contain 2 dull cyan bags, 1 wavy cyan bag, 2 light blue bags.
for line in open("day07.in"):
    container, contained = line.strip().split(" contain ")
    container = " ".join(container.split()[:2])

    for bag in contained.split(", "):
        if "no other bags" in bag:
            continue

        num, col1, col2, _ = bag.split()
        col = " ".join([col1, col2])
        inc = Inclusion(int(num), col)

        if container not in contains:
            contains[container] = []
        contains[container].append(inc)

        if col not in contained_by:
            contained_by[col] = set()
        contained_by[col].add(container)

# print(len(contains))

contains_gold = set()
current = contained_by["shiny gold"]
while len(current) > 0:
    n = set()
    for bag in current:
        contains_gold.add(bag)
        if bag in contained_by:
            n.update(contained_by[bag])
    current = n.difference(contains_gold)

print(len(contains_gold))

def contains_recursively(bag):
    count = 1
    if bag in contains:
        for num, color in contains[bag]:
            count += num * contains_recursively(color)
    
    return count


print(contains_recursively("shiny gold") - 1)
