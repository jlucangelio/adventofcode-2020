with open("day18.in") as f:
    LINES = f.read().splitlines()

def parse_paren_expr(stack):
    # print("parse_paren_expr:", stack)
    if stack[-1] != "(":
        print("parse_paren_expr: error: no (")
        print(stack)
        return None
    
    stack.pop()
    substack = []
    while stack[-1] != ")":
        if stack[-1] == "(":
            parse_paren_expr(stack)
    
        substack.append(stack.pop())
 
    rp = stack.pop()
    if rp != ")":
        print("parse_paren_expr: error: did not pop right paren")
        print(stack)
        return None

    substack.reverse()
    stack.append(parse_expr([], substack))
    return


def parse_expr(accum, stack):
    # print("parse_expr:", stack, accum)
    if len(stack) == 0:
        print("parse_expr: error: len(stack) == 0")
        return None

    if len(stack) == 1:
        if len(accum) == 0:
            return stack.pop()
        else:
            f = 1
            for a in accum:
                f *= a
            return f * stack.pop()

    if len(stack) == 2:
        print("parse_expr: error: len(stack) == 2")
        print(stack)
        return None

    if stack[-1] == "(":
        parse_paren_expr(stack)
    e1 = int(stack.pop())
    
    o = stack.pop()

    if stack[-1] == "(":
        parse_paren_expr(stack)
    e2 = int(stack.pop())

    if o == "+":
        stack.append(e1 + e2)
    elif o == "*":
        accum.append(e1)
        stack.append(e2)

    return parse_expr(accum, stack)


total = 0
# LINES = """2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2""".splitlines()

for line in LINES:
    stack = [c for c in line if c != " "]
    stack.reverse()
    partial = parse_expr([], stack)
    # print(partial)
    total += partial

print(total)
