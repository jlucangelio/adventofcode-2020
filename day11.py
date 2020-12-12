import copy

with open("day11.in") as f:
    SEATS = [[c for c in line.strip()] for line in f.readlines()]

def count_neighbors(pos, w, h, seats):
    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    occupied_neighbors = 0
    for d in directions:
        step = (pos[0] + d[0], pos[1] + d[1])
        if in_bounds(step, w, h) and seats[step[1]][step[0]] == "#":
           occupied_neighbors += 1

    return occupied_neighbors


def in_bounds(pos, w, h):
    x = pos[0]
    y = pos[1]
    return x >= 0 and x < w and y >= 0 and y < h


def count_neighbors_part2(pos, w, h, seats):
    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    occupied_neighbors = 0
    for d in directions:
        step = (pos[0] + d[0], pos[1] + d[1])
        while in_bounds(step, w, h):
            step_x = step[0]
            step_y = step[1]
            if seats[step_y][step_x] == ".":
                step = (step_x + d[0], step_y + d[1])
                continue
            else:
                if seats[step_y][step_x] == "#":
                    occupied_neighbors += 1
                break

    return occupied_neighbors


def count_occupied(neighbors, seats):
    return sum([1 for n in neighbors if seats[n[1]][n[0]] == "#"])


def one_step(seats, count_neighbors_func, crowded):
    h = len(seats)
    w = len(seats[0])

    new_seats = [[None for _ in range(len(seats[1]))] for _ in range(len(seats))]
    for j in range(h):
        for i in range(w):
            pos = (i, j)
            if seats[j][i] == '.':
                new_seats[j][i] = '.'
            elif seats[j][i] == 'L':
                if count_neighbors_func(pos, w, h, seats) == 0:
                    new_seats[j][i] = '#'
                else:
                    new_seats[j][i] = 'L'
            elif seats[j][i] == '#':
                if count_neighbors_func(pos, w, h, seats) >= crowded:
                    new_seats[j][i] = 'L'
                else:
                    new_seats[j][i] = '#'
    
    return new_seats


def same_seats(seats, other):
    for j in range(len(seats)):
        for i in range(len(seats[0])):
            if seats[j][i] != other[j][i]:
                return False
    
    return True


def count_total_occupied(seats):
    count = 0
    for j in range(len(seats)):
        for i in range(len(seats[0])):
            if seats[j][i] == '#':
                count += 1
    return count


seats = copy.deepcopy(SEATS)
while True:
    new_seats = one_step(seats, count_neighbors, 4)
    if same_seats(seats, new_seats):
        print(count_total_occupied(seats))
        break
    
    seats = new_seats

def print_seats(seats):
    for row in seats:
        print(row)
        print("".join(row))
    print()


seats = copy.deepcopy(SEATS)
while True:
    new_seats = one_step(seats, count_neighbors_part2, 5)
    if same_seats(seats, new_seats):
        print(count_total_occupied(seats))
        break
    
    seats = new_seats
