import math

# BOARDING_PASSES = ["FBFBBFFRLR"]
BOARDING_PASSES = [line.strip() for line in open("day05.in").readlines()]

NROWS = 128
NCOLS = 8

def binary_search(floor_inc, ceil_exc, directions):
    temp_f = floor_inc
    temp_c = ceil_exc

    for i in range(len(directions)):
        pivot = (temp_f + temp_c) // 2
        if directions[i] == "F" or directions[i] == "L":
            temp_c = pivot
        elif directions[i] == "B" or directions[i] == "R":
            temp_f = pivot
        # print(temp_f, temp_c, directions[i])
    
    if temp_f == temp_c - 1:
        return temp_f
    else:
        return None


def seat_id(boarding_pass):
    row = binary_search(0, NROWS, boarding_pass[0:7])
    col = binary_search(0, NCOLS, boarding_pass[7:])
    return row * 8 + col

seat_ids = [seat_id(bp) for bp in BOARDING_PASSES] 
print(max(seat_ids))

prev = None
for seat_id in sorted(seat_ids):
    if prev != None:
        if seat_id == prev + 2:
            print(prev + 1)
            break
    
    prev = seat_id
