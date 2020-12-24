from collections import deque
from copy import copy

INPUT = "219347865"
# INPUT = "389125467"

cups = deque([int(c) for c in INPUT])
print(len(cups))
print(cups[-1])

cur_pos = 0
min_cup = 1
max_cup = max(cups)
removed = [0, 0, 0]
range_3 = range(3)
len_cups = len(cups)

for i in range(100):
    cur = cups[cur_pos]
    if cur_pos > len_cups // 2:
        cups.rotate(len_cups - cur_pos - 1)
    else:
        cups.rotate(-(cur_pos + 1))
    cur_pos = len_cups - 1
    for j in range_3:
        r = cups.popleft()
        removed[j] = r
        if r == max_cup:
            max_cup -= 1
        elif r == min_cup:
            min_cup += 1

    dest = cur - 1
    for _ in range_3:
        if dest != 0 and dest not in removed:
            break
        else:
            if dest > min_cup:
                dest -= 1
            else:
                dest = max_cup

    pos = cups.index(dest)
    if pos > len_cups // 2:
        cups.rotate(len_cups - 3 - pos - 1)
    else:
        cups.rotate(-(pos + 1))

    for l in range_3:
        to_insert = removed[2 - l]
        if to_insert > max_cup:
            max_cup = to_insert
        elif to_insert < min_cup:
            min_cup = to_insert
        cups.appendleft(to_insert)

    cur_pos = (((len_cups - 1) - (pos + 1)) + 1) % len_cups

if len(cups) == 9:
    print()
    print(cups)
    cups.rotate(-cups.index(1))
    print(cups)
    print("".join([str(i) for i in list(cups)[1:]]))
