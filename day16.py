rules = {}

with open("day16.in") as f:
    lines = f.read().splitlines()

# print(lines)

for i, line in enumerate(lines):
    # departure location: 28-184 or 203-952
    if line == "":
        break

    field, values = line.split(": ")
    range1, range2 = values.split(" or ")
    rules[field] = (tuple([int(t) for t in range1.split("-")]),
                    tuple([int(t) for t in range2.split("-")]))

# print(i)
for j, line in enumerate(lines[i+2:]):
    if line == "":
        break
    my_ticket = [int(t) for t in line.split(",")]

# print(j)

def invalid(v, r):
    return not(v >= r[0][0] and v <= r[0][1] or v >= r[1][0] and v <= r[1][1])


ranges = rules.values()
invalid_values = []
valid_tickets = []
fields = [[] for _ in lines[i+j+4].split(",")]
for line in lines[i+j+4:]:
    found_invalid = False
    ticket = [int(t) for t in line.split(",")]
    for n in ticket:
        if all([invalid(n, r) for r in ranges]):
            invalid_values.append(n)
            found_invalid = True
    
    if not found_invalid:
        valid_tickets.append(ticket)
        for i, e in enumerate(ticket):
            fields[i].append(e)
        found_invalid = False

print(sum(invalid_values))

for i, e in enumerate(my_ticket):
    fields[i].append(e)

names_to_indexes = {}
for rule, ranges in rules.items():
    for i, field in enumerate(fields):
        for v in field:
            if invalid(v, ranges):
                break
        else:
            if rule not in names_to_indexes:
                names_to_indexes[rule] = set()
            
            names_to_indexes[rule].add(i)

name_to_index = {}
while any([len(v) > 1 for v in names_to_indexes.values()]):
    name = min(names_to_indexes, key=lambda k: len(names_to_indexes[k]))
    indexes = names_to_indexes[name]
    if len(indexes) > 1:
        print("error: lowest count is > 1")
        break

    index = indexes.pop()
    name_to_index[name] = index
    for k in names_to_indexes:
        names_to_indexes[k].discard(index)

    del names_to_indexes[name]

p = 1
for k in name_to_index:
    if "departure" in k:
        p *= my_ticket[name_to_index[k]]

print(p)
