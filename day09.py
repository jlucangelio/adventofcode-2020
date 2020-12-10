with open("day09.in") as f:
    INPUT = [int(n) for n in f.readlines()]

for i in range(25, len(INPUT)):
    found = False
    for j in range(i - 25, i):
        for k in range(i - 25, i):
            if j < k:
                if INPUT[j] + INPUT[k] == INPUT[i]:
                    found = True
                    break
        if found:
            break

    if found == False:
        idx = i
        num = INPUT[i]
        print(num)
        break

sums = {}
def calculate_sum(i, j):
    neighbors = [((i - 1, j), -INPUT[i-1]),
                 ((i, j - 1), INPUT[j])]

    s = 0
    for n, v in neighbors:
        if n in sums:
            s = sums[n] + v
            break
    else:
        s = sum(INPUT[i:j+1])

    sums[(i, j)] = s
    return s


found = False
for i in range(len(INPUT)):
    for j in range(i + 1, len(INPUT)):
        if calculate_sum(i, j) == num:
            print(min(INPUT[i:j+1]) + max(INPUT[i:j+1]))
            found = True
            break
    
    if found:
        break
