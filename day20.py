import copy
import math

with open("day20.in") as f:
# with open("day20_small.in") as f:
    LINES = f.read().splitlines()

class Tile:
    def __init__(self, l):
        if len(l) != len(l[0]):
            print("error: tile is not square")

        self._data = l
        self.width = len(l[0])
        self.height = len(l)
        self._rtop = self._data[0][::-1]
        self._rbottom = self._data[-1][::-1]
        self._left = "".join([row[0] for row in self._data])
        self._rleft = self._left[::-1]
        self._right = "".join([row[-1] for row in self._data])
        self._rright = self._right[::-1]


    def top(self, reversed=False):
        if reversed:
            return self._rtop
        else:
            return self._data[0]


    def bottom(self, reversed=False):
        if reversed:
            return self._rbottom
        else:
            return self._data[-1]


    def left(self, reversed=False):
        if reversed:
            return self._rleft
        else:
            return self._left


    def right(self, reversed=False):
        if reversed:
            return self._rright
        else:
            return self._right


    def flip_h(self):
        # ab
        # cd

        # ba
        # dc
        new_data = []
        for r in self._data:
            new_data.append(r[::-1])
        return Tile(new_data)


    def flip_v(self):
        # ab
        # cd

        # cd
        # ab
        nrows = len(self._data)
        new_data = []
        for i in range(1, nrows + 1):
            new_data.append(self._data[nrows - i])
        return Tile(new_data)


    def flip_both(self):
        # ab
        # cd

        # dc
        # ba
        pass


    def rot_90(self):
        # ab
        # cd

        # ca
        # db
        new_data = [[None for _ in range(len(self._data))] for _ in range(len(self._data))]
        for ridx, row in enumerate(self._data):
            for cidx, _ in enumerate(row):
                new_data[cidx][len(self._data) - ridx - 1] = self._data[ridx][cidx]

        for ridx in range(len(new_data)):
            new_data[ridx] = "".join(new_data[ridx])

        return Tile(new_data)


    def rot_180(self):
        # ab
        # cd

        # dc
        # ba
        return self.rot_90().rot_90()


    def rot_270(self):
        # ab
        # cd

        # bd
        # ac
        return self.rot_180().rot_90()


    def flip_tl_br(self):
        # abc
        # def
        # ghi

        # adg
        # beh
        # cfi
        return self.flip_v().rot_90()


    def flip_tr_bl(self):
        # ab
        # cd

        # db
        # ca
        return self.flip_h().rot_90()


    def __str__(self):
        return "\n".join(self._data)


    def data(self):
        return self._data


tiles = {}
for i in range(0, (len(LINES) // 12) + 1):
    # print(LINES[12*i])
    # Tile 1297:
    tile_no = int(LINES[12*i].split()[1][:4])
    tiles[tile_no] = Tile(LINES[12*i+1:12*i+11])

def match_tiles(t, u):
    SIDES = [(m, r) for m in [Tile.left, Tile.right, Tile.top, Tile.bottom] for r in [True, False]]

    for m, r in SIDES:
        for n, s in SIDES:
            if m(t, reversed=r) == n(u, reversed=s):
                return True

    return False


VARIATIONS = [lambda t: t, Tile.flip_h, Tile.flip_v, Tile.rot_90, Tile.rot_180,
              Tile.rot_270, Tile.flip_tl_br, Tile.flip_tr_bl]


def match_and_rotate_tiles(tiles, t1, t2, edge1, edge2):
    for v1 in VARIATIONS:
        new_t1 = v1(tiles[t1])
        for v2 in VARIATIONS:
            new_t2 = v2(tiles[t2])
            if edge1(new_t1) == edge2(new_t2):
                return (new_t1, new_t2)

    # print("match_and_rotate_tiles: could not find match")
    return None


def match_and_rotate_second_tile(tiles, tile1, t2, edge1, edge2):
    for v2 in VARIATIONS:
        new_t2 = v2(tiles[t2])
        if edge1(tile1) == edge2(new_t2):
            # print("match")
            return new_t2

    # print("match_and_rotate_second_tile: could not find match")
    return None


corners = []
l = int(math.sqrt(len(tiles)))
print("l", l)
arranged_tiles = [[None for _ in range(l)] for _ in range(l)]
neighbors = {}
for t_id, t in tiles.items():
    matched_tiles = set()

    for u_id, u in tiles.items():
        if t_id == u_id:
            continue

        if match_tiles(t, u):
            matched_tiles.add(u_id)

    neighbors[t_id] = matched_tiles

    if len(matched_tiles) == 2:
        print(t_id)
        # print(matched_tiles)
        corners.append(t_id)

p = 1
for t_id in corners:
    p *= t_id

print(p)
# print(corners)

W = len(arranged_tiles[0])
H = len(arranged_tiles)

def rearrange_tiles(tiles, neighbors):
    top_left_id = corners[0]
    top_left = tiles[top_left_id]

    for v in VARIATIONS:
        opt = v(top_left)
        final_ids = [[None for _ in range(l)] for _ in range(l)]
        final_tiles = [[None for _ in range(l)] for _ in range(l)]
        final_ids[0][0] = top_left_id
        final_tiles[0][0] = opt

        for i in range(1, W - 1):
            prev_id = final_ids[0][i - 1]
            prev_tile = final_tiles[0][i - 1]
            if prev_id is None:
                print("rearrange_tiles_better: error: prev is None")
                break

            candidates = set()
            for candidate in neighbors[prev_id]:
                candidate_neighbors = copy.copy(neighbors[candidate])
                candidate_neighbors.discard(prev_id)

                if len(candidate_neighbors) == 2:
                    candidates.add(candidate)

            for c in candidates:
                right_tile = match_and_rotate_second_tile(tiles, prev_tile, c,
                                                          Tile.right, Tile.left)
                if right_tile is not None:
                    final_ids[0][i] = c
                    final_tiles[0][i] = right_tile

            if final_tiles[0][i] is None:
                print("rearrange_tiles_better: error: could not find neighbor",
                      0, i)
                break

        if final_tiles[0][W - 2] is None:
            continue

        prev_id = final_ids[0][W - 2]
        prev_tile = final_tiles[0][W - 2]
        prev_neighbors = copy.copy(neighbors[prev_id])
        possible_top_right = prev_neighbors.intersection(corners)
        if len(possible_top_right) != 1:
            print("rearrange_tiles: error: not exactly one top right corner available")
            return None

        top_right_id = possible_top_right.pop()
        top_right = match_and_rotate_second_tile(tiles, prev_tile, top_right_id,
                                                 Tile.right, Tile.left)
        if top_right is None:
            print("rearrange_tiles_better: error: could not rotate top right")
            continue

        final_ids[0][W - 1] = top_right_id
        final_tiles[0][W - 1] = top_right

        for j in range(1, H):
            for i in range(0, W):
                up_id = final_ids[j - 1][i]
                up_tile = final_tiles[j - 1][i]
                candidate_set = neighbors[up_id]
                for candidate in candidate_set:
                    bottom_tile = match_and_rotate_second_tile(tiles, up_tile, candidate,
                                                            Tile.bottom, Tile.top)
                    if bottom_tile is not None:
                        break
                if bottom_tile is None:
                    print("rearrange_tiles_better: could not rotate bottom tile", i, j)
                    break

                final_ids[j][i] = candidate
                final_tiles[j][i] = bottom_tile

            if final_ids[j][-1] is None:
                break

        if final_ids[-1][-1] is not None:
            break

    return final_ids, final_tiles


def print_tiles(arranged_tiles):
    for tile_row in arranged_tiles:
        for pixel_row_jdx, _ in enumerate(tile_row[0].data()):
            print(" ".join([t.data()[pixel_row_jdx] for t in tile_row]))

        print()

final_ids, final_tiles = rearrange_tiles(tiles, neighbors)
print(final_ids)
print()
print_tiles(final_tiles)

def combine_tiles(arranged_tiles):
    data = []
    for tile_row in arranged_tiles:
        for pixel_row_jdx, _ in enumerate(tile_row[0].data()):
            if pixel_row_jdx == 0 or pixel_row_jdx == len(tile_row[0].data()) - 1:
                continue
            data.append("".join([t.data()[pixel_row_jdx][1:-1] for t in tile_row]))
    return data


image_data = combine_tiles(final_tiles)
print("\n".join(image_data))
print()

image = Tile(image_data)

SEA_MONSTER = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()
sm_width = len(SEA_MONSTER[0])
sm_height = len(SEA_MONSTER)
sm_pixels = sum([r.count("#") for r in SEA_MONSTER])
print(sm_pixels)

for v in VARIATIONS:
    img = v(image)
    sm_count = 0

    for top_left_y in range(0, img.height - sm_height + 1):
        for top_left_x in range(0, img.width - sm_width + 1):
            found = True
            for y in range(sm_height):
                for x in range(sm_width):
                    if (SEA_MONSTER[y][x] == "#" and
                        img.data()[top_left_y + y][top_left_x + x] != "#"):
                            found = False
                            break
                if not found:
                    break
            else:
                sm_count +=1

    if sm_count > 0:
        print(v, sm_count)
        print(sum([r.count("#") for r in img.data()]) - sm_count * sm_pixels)
        break
