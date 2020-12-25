CARD_PK = 14012298
DOOR_PK = 74241

# CARD_PK = 5764801
# DOOR_PK = 17807724

def transform(subject_number, remainder, loop_max):
    v = 1
    for i in range(loop_max):
        v *= subject_number
        v %= 20201227

        if v == remainder:
            return (i+1)

    return None

door_loop_count = transform(7, DOOR_PK, 1_000_000_000)
print(door_loop_count)

v = 1
for i in range(door_loop_count):
    v *= CARD_PK
    v %= 20201227

print(v)