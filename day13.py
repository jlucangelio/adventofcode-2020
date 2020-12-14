DEPART = 1000677
SCHEDULE = "29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,661,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,521,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"

buses = [int(t) for t in SCHEDULE.split(",") if t != "x"]

waits = [(((DEPART // b) + 1) * b - DEPART, b) for b in buses]
earliest = min(waits, key=lambda v: v[0])
print(earliest[0] * earliest[1])

buses = SCHEDULE.split(",")

a_s = []
n_s = []

for i, b in enumerate(buses):
    if b != "x":
        b = int(b)
        if i == 0:
            print("x = %d mod %d" % (i, b))
            a_s.append(i)
            n_s.append(b)
        else:
            if b - i < 0:
                r = -i % b
            else:
                r = b - i 
            print("x = %d mod %d" % (r, b))
            a_s.append(r)
            n_s.append(b)


from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


print(chinese_remainder(n_s, a_s))
