with open("day08.in") as f:
    INSTRUCTIONS = [line.strip() for line in f.readlines()]

def execute(instrs):
    pc = 0
    acc = 0

    visited = set()

    while pc not in visited and pc < len(instrs):
        visited.add(pc)

        op, arg = instrs[pc].split()
        if op == "nop":
            pc += 1
        elif op == "acc":
            acc += int(arg)
            pc += 1
        elif op == "jmp":
            pc += int(arg)

    if pc in visited:
        return (acc, False)
    elif pc == len(instrs):
        return (acc, True)
    else:
        return None


print(execute(INSTRUCTIONS))

for i in range(len(INSTRUCTIONS)):
    instr = INSTRUCTIONS[i]
    op, arg = instr.split()
    if op == "nop":
        INSTRUCTIONS[i] = "jmp " + arg
    elif op == "jmp":
        INSTRUCTIONS[i] = "nop " + arg
    else:
        continue

    acc, completed = execute(INSTRUCTIONS)
    INSTRUCTIONS[i] = instr

    if completed:
        print(acc, completed)
        break
