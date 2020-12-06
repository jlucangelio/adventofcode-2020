import functools

forest = []

with open("day03.in") as f:
    for line in f:
        forest.append([c == "#" for c in line.strip()])

def access(forest, pos):
    return forest[pos[0]][pos[1] % len(forest[pos[0]])]


def down(pos, slope):
    return (pos[0] + slope[0], pos[1] + slope[1])


def count_trees(forest, slope):
    pos = (0, 0)
    count = 0

    while pos[0] < len(forest):
        if access(forest, pos):
            count += 1
        pos = down(pos, slope)

    return count


SLOPE = (1, 3)
print(count_trees(forest, SLOPE))

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
counts = [count_trees(forest, slope) for slope in slopes]
print(counts)
print(functools.reduce(lambda x, y: x*y, counts))
