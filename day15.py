INPUT = [int(t) for t in "11,0,1,10,5,19".split(",")]

spoken = INPUT[:]
last_spoken = dict([(e, [i + 1, None]) for i, e in enumerate(INPUT)])
r = len(INPUT) + 1

most_recently_last_spoken = spoken[-1]
# while r < 2021:
while r < 30000001:
    if r % 1000000 == 0:
        print(r)

    l = most_recently_last_spoken
    if l in last_spoken:
        turns = last_spoken[l]
        if turns[1] is None:
            to_speak = 0
        else:
            to_speak = turns[1] - turns[0]
    else:
        print(l)
        raise "spoken number not added to last_spoken"

    if r == 2020 or r == 30000000:
        print("to speak", to_speak)

    most_recently_last_spoken = to_speak

    if to_speak in last_spoken:
        turns = last_spoken[to_speak]
        if turns[1] is not None:
            turns[0] = turns[1]
        turns[1] = r
    else:
        last_spoken[to_speak] = [r, None]
    
    r += 1
