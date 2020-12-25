from collections import deque
from copy import copy

INPUT = "219347865"
# INPUT = "389125467"

next_cup = [None for i in range(1_000_001)]
for c in range(1, 10):
    n = INPUT[(INPUT.index(str(c)) + 1) % len(INPUT)]
    next_cup[c] = int(n)

next_cup[int(INPUT[-1])] = 10

for c in range(10, 1_000_000):
    next_cup[c] = c + 1

next_cup[1_000_000] = int(INPUT[0])

cur = int(INPUT[0])
min_cup = 1
max_cup = len(next_cup) - 1
removed = [0, 0, 0]
range_3 = range(3)
print(min_cup, max_cup)

print(cur)
for i in range(10_000_000):
    # print(cur)
    n = cur
    for j in range_3:
        n = next_cup[n]
        removed[j] = n
        if n == max_cup:
            max_cup -= 1
        elif n == min_cup:
            min_cup += 1
        # print(n)

    # print(removed)

    dest = cur - 1
    for _ in range_3:
        if dest != 0 and dest not in removed:
            break
        else:
            if dest > min_cup:
                dest -= 1
            else:
                dest = max_cup

    # print(dest)
    # print()

    next_dest = next_cup[dest]
    next_last_removed = next_cup[removed[-1]]
    next_cup[dest] = removed[0]
    next_cup[removed[-1]] = next_dest
    next_cup[cur] = next_last_removed

    for r in removed:
        if r > max_cup:
            max_cup = r
        elif r < min_cup:
            min_cup = r

    cur = next_cup[cur]

if len(next_cup) == 10:
    n = 1
    l = []
    for _ in range(len(next_cup) - 2):
        n = next_cup[n]
        l.append(str(n))

    print("".join(l))

print(next_cup[1])
print(next_cup[next_cup[1]])
print(next_cup[1] * next_cup[next_cup[1]])
