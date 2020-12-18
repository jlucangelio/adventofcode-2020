from collections import defaultdict, namedtuple
from copy import copy

Coord = namedtuple("Coord", "x y z")

DIRECTIONS = [Coord(i, j, k) for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2) if i != 0 or j != 0 or k != 0]

def neighbor(c, d):
    return Coord(c.x + d.x, c.y + d.y, c.z + d.z)


def count_active_neighbors(c, state):
    return sum([int(state[neighbor(c, d)] == "#") for d in DIRECTIONS])    


def update_limit(l, v):
    return (min(l[0], v - 1), max(l[1], v + 1))


with open("day17.in") as f:
    LINES = f.read().splitlines()

# LINES = """.#.
# ..#
# ###""".splitlines()

upper_y = None
STATE = defaultdict(lambda: ".")
for i, l in enumerate(LINES):
    upper_y = len(l)
    for j, c in enumerate(l):
        STATE[Coord(len(LINES) - i - 1, j, 0)] = c

limit_x = (-1, len(LINES))
limit_y = (-1, upper_y)
limit_z = (-1, 1)

print(limit_x, limit_y, limit_z)

cur_state = copy(STATE)
for _ in range(6):
    new_state = defaultdict(lambda: ".")

    for i in range(limit_x[0], limit_x[1] + 1):
        for j in range(limit_y[0], limit_y[1] + 1):
            for k in range(limit_z[0], limit_z[1] + 1):
                c = Coord(i, j, k)
                s = cur_state[c]
                active_neighbors = count_active_neighbors(c, cur_state)
                if (s == "#" and (active_neighbors == 2 or active_neighbors == 3) or
                    s == "." and active_neighbors == 3):
                        new_state[c] = "#"
                        limit_x = update_limit(limit_x, c.x)
                        limit_y = update_limit(limit_y, c.y)
                        limit_z = update_limit(limit_z, c.z)

    cur_state = new_state

print(len(cur_state))
