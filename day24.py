from collections import defaultdict

EW = ["e", "w"]
NS = ["n", "s"]
DIRS = set(["e", "se", "sw", "w", "nw", "ne"])
OP = {
    "e": "w",
    "w": "e",
    "n": "s",
    "s": "n",
    "se": "nw",
    "sw": "ne",
    "ne": "sw",
    "nw": "se",
}

EQUIVALENTS = {}
def populate_equivalents():
    for d in DIRS:
        eqs = {}
        eqs[d] = [d, d]
        eqs[OP[d]] = []

        if len(d) == 1:
            for ns in NS:
                eqs[ns + d] = None
        elif len(d) == 2:
            eqs[d[1]] = None
            eqs[d[0] + OP[d[1]]] = None

        if len(d) == 1:
            for ns in NS:
                eqs[ns + OP[d]] = [ns + d]
        elif len(d) == 2:
            eqs[OP[d[1]]] = [d[0] + OP[d[1]]]
            eqs[OP[d[0]] + d[1]] = [d[1]]

        EQUIVALENTS[d] = eqs


OPPOSITES = {
    "e": ("w", ("nw", "sw")),
    "w": ("e", ("ne", "se")),
    "se": ("nw", ("w", "ne")),
    "sw": ("ne", ("e", "sw")),
    "ne": ("sw", ("e", "nw")),
    "nw": ("se", ("w", "se"))
}

def directions(s):
    # esenee
    last = ""
    for c in s:
        if c == "e" or c == "w":
            if last == "":
                yield c
            else:
                yield last + c
                last = ""
        elif c == "s" or c == "n":
                last = c


def canonicalize(ds, s):
    for d in directions(s):
        # if the opposite of this direction is already in,
        # just remove one instance.
        direct_op, combined_op = OPPOSITES[d]
        if ds[direct_op] > 0:
            ds[direct_op] -= 1
        # If two directions combine to be the opposite of this direction,
        # just remove them.
        elif ds[combined_op[0]] > 0 and ds[combined_op[1]] > 0:
            ds[combined_op[0]] -= 1
            ds[combined_op[1]] -= 1
        else:
            # Now replace directions with shorter equivalents.
            for e, eq in EQUIVALENTS[d].items():
                if eq is not None and len(eq) == 1 and ds[e] > 0:
                    ds[e] -= 1
                    ds[eq[0]] += 1
                    break
            else:
                ds[d] += 1

    for d in DIRS:
        if d not in ds:
            ds[d] = 0

    return frozenset(ds.items())


def move_and_canonicalize(fs, d):
    return canonicalize(dict(fs), d)


def neighbors(t):
    return [move_and_canonicalize(t, d) for d in DIRS]


def count_black_neighboring_tiles(t, black_tiles):
    return sum([1 for n in neighbors(t) if n in black_tiles])


with open("day24.in") as f:
    LINES = f.read().splitlines()

# LINES = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew""".splitlines()

black_tiles = set()

populate_equivalents()

for line in LINES:
    tile_id = canonicalize(defaultdict(int), line)
    # print(tile_id)
    if tile_id in black_tiles:
        black_tiles.remove(tile_id)
    else:
        black_tiles.add(tile_id)

print(len(black_tiles))

for day in range(100):
    next_day = set()

    for tile in black_tiles:
        if 0 < count_black_neighboring_tiles(tile, black_tiles) <= 2:
            next_day.add(tile)

        for n in neighbors(tile):
            if n in black_tiles:
                # If |n| was in |black_tiles|, we already have looked/
                # will look at it in the 'if' statement above.
                continue

            # Tile is white.
            nblack_tiles = count_black_neighboring_tiles(n, black_tiles)
            if nblack_tiles == 2:
                next_day.add(n)

    # print(day + 1, len(next_day))
    black_tiles = next_day

print(len(black_tiles))
