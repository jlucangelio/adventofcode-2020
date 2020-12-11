from copy import copy

with open("day10.in") as f:
    ADAPTERS = set([int(line.strip()) for line in f.readlines()])

# print(len(ADAPTERS))

used = [0]
diffs = []
def try_all_adapters(used, diffs, available):
    if len(available) == 0:
        print(diffs.count(1) * (diffs.count(3) + 1))
        return

    l = used[-1]
    for a in available:
        diff = a - l
        if diff > 0 and diff <= 3:
            used.append(a)
            diffs.append(diff)
            available.remove(a)
            try_all_adapters(used, diffs, available)
            if len(available) == 0:
                break
            diffs.pop()
            available.add(used.pop())


try_all_adapters(used, diffs, copy(ADAPTERS))

counts = {}
def count_combinations(adapters, first, last):
    if (first, last) in counts:
        return counts[(first, last)]
    
    if last == first:
        counts[(first, last)] = 1
        return 1

    if last - first == 1:
        counts[(first, last)] = 1
        return 1
    
    if last - first == 2:
        count = 1
        if first + 1 in adapters:
            count += 1
        counts[(first, last)] = count
        return count

    count = 0
    for i in range(1, 4):
        if first + i in adapters:
            count += count_combinations(adapters, first + i, last)
    
    counts[(first, last)] = count
    return count


print(count_combinations(ADAPTERS.union([0]), 0, max(ADAPTERS)))
