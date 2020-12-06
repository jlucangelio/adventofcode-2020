total_part1 = 0
total_part2 = 0

with open("day02.in") as f:
    for line in f:
        # 2-4 x: xxxwxx
        policy, password = line.strip().split(': ')
        reps, letter = policy.split()
        lower, upper = reps.split('-')
        lower = int(lower)
        upper = int(upper)
        if password.count(letter) >= lower and password.count(letter) <= upper:
            total_part1 += 1
        
        if (password[lower-1] == letter) + (password[upper-1] == letter) == 1:
            total_part2 += 1

print(total_part1)
print(total_part2)
