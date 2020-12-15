# x AND 1 = x
# x OR 0 = x

memory = {}
with open("day14.in") as f:
    for line in f.readlines():
        instr, op = line.strip().split(" = ")

        if "mask" in instr:
            # mask = 1001X0XX1101100X101XX00111000000X100
            mask_and = 0
            mask_or = 0
            for digit in op:
                mask_and <<= 1
                mask_or <<= 1
                if digit == "1":
                    mask_and |= 0b1
                    mask_or |= 0b1
                elif digit == "0":
                    pass
                elif digit == "X":
                    mask_and |= 0b1

            # print("      " + op)
            # print("and " + bin(mask_and))
            # print("or  " + bin(mask_or))
            # print()
        else:
            # mem[34342] = 4318
            val = int(op)
            location = int(instr.split("[")[1][:-1])
            final_value = (val | mask_or) & mask_and
            memory[location] = final_value

print(sum(memory.values()))

def expand_floating_bits(value, x_s):
    if len(x_s) == 0:
        return [value]

    res = []
    mask = 1 << x_s[0]
    res.extend(expand_floating_bits(value & ~mask, x_s[1:]))
    res.extend(expand_floating_bits(value | mask, x_s[1:]))
    return res


memory = {}
with open("day14.in") as f:
    for line in f.readlines():
        instr, op = line.strip().split(" = ")

        if "mask" in instr:
            # mask = 1001X0XX1101100X101XX00111000000X100
            orig_mask = op
            mask = 0
            x_s = []
            for idx, digit in enumerate(op):
                mask <<= 1
                if digit == "1":
                    mask |= 0b1
                elif digit == "0":
                    pass
                elif digit == "X":
                    x_s.append(35 - idx)

        else:
            # mem[34342] = 4318
            val = int(op)
            location = int(instr.split("[")[1][:-1])
            locations = expand_floating_bits(location | mask, x_s)
            for l in locations:
                memory[l] = val

print(sum(memory.values()))
