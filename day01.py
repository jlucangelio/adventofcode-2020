with open("day01.in") as f:
    expenses = [int(l.strip()) for l in f.readlines()]

for e in expenses:
    for f in expenses:
        if e + f == 2020:
            print(e * f)
            break

for e in expenses:
    for f in expenses:
        for g in expenses:
            if e + f + g == 2020:
                print(e * f * g)
                break
