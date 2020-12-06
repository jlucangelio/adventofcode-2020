lines = None
with open("day04.in") as f:
#with open("day04_small.in") as f:
    lines = [line.strip() for line in f.readlines()]

REQUIRED_FIELDS = set(["byr",
                       "iyr",
                       "eyr",
                       "hgt",
                       "hcl",
                       "ecl",
                       "pid"])

def between(floor, n, ceiling):
    return n >= floor and n <= ceiling


def validate_year(year, floor, ceiling):
    return len(year) == 4 and between(floor, int(year), ceiling)


def validate_byr(byr):
    return validate_year(byr, 1920, 2002)


def validate_iyr(iyr):
    return validate_year(iyr, 2010, 2020)


def validate_eyr(eyr):
    return validate_year(eyr, 2020, 2030)


def validate_hgt(hgt):
    if "cm" in hgt:
        hnum =int(hgt[0:hgt.find("cm")])
        return between(150, hnum, 193)
    elif "in" in hgt:
        hnum = int(hgt[0:hgt.find("in")])
        return between(59, hnum, 76)
    return False


def validate_hcl(hcl):
    return hcl[0] == "#" and all([c in "abcdef0123456789" for c in hcl[1:]])


def validate_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(pid):
    return len(pid) == 9


VALIDATORS = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid,
    "cid": lambda x: True
}

passport = {}
valid_passports = []
for line in lines:
    # print(line)
    if line == "":
        if REQUIRED_FIELDS <= passport.keys():
            valid_passports.append(passport)
        passport = {}
        continue

    for item in line.split():
        k, v = item.split(":")
        #print(k, v)
        passport[k] = v

#print(valid_passports)
print(len(valid_passports))

passport = {}
valid_passports = []
for line in lines:
    # print(line)
    if line == "":
        if REQUIRED_FIELDS <= passport.keys():
            if all([VALIDATORS[k](passport[k]) for k in passport.keys()]):
                valid_passports.append(passport)
        passport = {}
        continue

    for item in line.split():
        k, v = item.split(":")
        #print(k, v)
        passport[k] = v

print(len(valid_passports))
