answers = set()
total = 0
for line in open("day06.in"):
    line = line.strip()
    if line == "":
        total += len(answers)
        answers.clear()
        continue

    answers.update(line)

print(total)

answers.clear()
total = 0
first = True
for line in open("day06.in"):
    line = line.strip()
    if line == "":
        total += len(answers)
        answers.clear()
        first = True
        continue

    if first:
        answers.update([c for c in line])
        first = False
    else:
        answers.intersection_update(line)

print(total)
