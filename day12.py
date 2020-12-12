from collections import namedtuple

with open("day12.in") as f:
    INSTRUCTIONS = [line.strip() for line in f.readlines()]

Pos = namedtuple("Pos", "x y")

Dir = namedtuple("Dir", "x y")
N = Dir(0, 1)
S = Dir(0, -1)
E = Dir(1, 0)
W = Dir(-1, 0)

directions = {"N": N, "S": S, "E": E, "W": W}

rotations = {"L90": Dir(0, 1),
             "L180": Dir(-1, 0),
             "L270": Dir(0, -1),
             "R90": Dir(0, -1),
             "R180": Dir(-1, 0),
             "R270": Dir(0, 1)}

def scale(k, d):
    return Dir(k * d.x, k * d.y)


def move(p, m):
    return Pos(p.x + m.x, p.y + m.y)


def rotate(d, r):
    a = d.x
    b = d.y
    c = r.x
    d = r.y

    return Dir(a*c - b*d, a*d + b*c)

pos = Pos(0, 0)
direction = E
for ins in INSTRUCTIONS:
    a = ins[0]
    val = int(ins[1:])

    if a == "N" or a == "S" or a == "E" or a == "W" or a == "F":
        if a == "F":
            d = direction
        else:
            d = directions[a]
        pos = move(pos, scale(val, d))
    elif a == "L" or a == "R":
        direction = rotate(direction, rotations[ins])

print(abs(pos.x) + abs(pos.y))

pos = Pos(0, 0)
waypoint = Dir(10, 1)
for ins in INSTRUCTIONS:
    a = ins[0]
    val = int(ins[1:])

    if a == "N" or a == "S" or a == "E" or a == "W":
        d = directions[a]
        waypoint = move(waypoint, scale(val, d))
    elif a == "F":
        pos = move(pos, scale(val, waypoint))
    elif a == "L" or a == "R":
        waypoint = rotate(waypoint, rotations[ins])

print(abs(pos.x) + abs(pos.y))
