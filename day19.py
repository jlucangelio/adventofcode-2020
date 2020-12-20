import re

rules = {}

with open("day19.in") as f:
    LINES = f.read().splitlines()

for i, l in enumerate(LINES):
    if l == "":
        break

    # 58: 127 99 | 105 36
    number, r = l.split(": ")
    if "\"" in r:
        rule = r[1]
    else:
        rule = {tuple([int(r) for r in opt.split()]) for opt in r.split(" | ")}

    rules[int(number)] = rule

def build_regexp(n, rules, part2=False):
    rule = rules[n]
    if type(rule) == str:
        return rule
    
    if part2:
        #8: 42 | 42 8
        #11: 42 31 | 42 11 31
        r_42 = build_regexp(42, rules)
        if n == 8:
            return "(" + r_42 + "+" + ")"

        if n == 11:
            r_31 = build_regexp(31, rules)
            #42{1}31{1}|42{2}31{2}|...
            return "(" + "|".join([r_42 + "{%d}" % i + r_31 + "{%d}" % i for i in range(1, 10)]) + ")"

    return "(" + "|".join(["".join([build_regexp(c, rules, part2) for c in opt]) for opt in rule]) + ")"


r = re.compile(build_regexp(0, rules))
r_part2 = re.compile(build_regexp(0, rules, part2=True))

count = 0
count_part2 = 0

for l in LINES[i+1:]:
    if r.fullmatch(l) is not None:
        count += 1
    if r_part2.fullmatch(l) is not None:
        count_part2 += 1

print(count)
print(count_part2)
