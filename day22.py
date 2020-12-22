from collections import deque
from copy import copy

with open("day22.in") as f:
    LINES = f.read().splitlines()

# LINES = """Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10""".splitlines()

for i, l in enumerate(LINES):
    if l == "":
        break

initial_deck1 = deque([int(c) for c in LINES[1:i]])
initial_deck2 = deque([int(c) for c in LINES[i+2:]])

def combat(deck1, deck2, recursive=False, level=0):
    previous_states = set()

    while len(deck1) > 0 and len(deck2) > 0:
        state = (tuple(deck1), tuple(deck2))
        if state in previous_states:
            # If we've seen this state before, player 1 wins.
            return True, deck1, deck2

        previous_states.add(state)

        c1 = deck1.popleft()
        c2 = deck2.popleft()
        p1_wins = None
        if recursive and c1 <= len(deck1) and c2 <= len(deck2):
            # Recurse.
            sub_deck1 = deque()
            sub_deck2 = deque()
            for i in range(c1):
                sub_deck1.append(deck1[i])
            for i in range(c2):
                sub_deck2.append(deck2[i])

            p1_wins, _, _ = combat(sub_deck1, sub_deck2, True, level + 1)
        else:
            # Regular combat.
            p1_wins = c1 > c2

        if p1_wins:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    return len(deck2) == 0, deck1, deck2


for recursive in [False, True]:
    p1_wins, final_deck1, final_deck2 = combat(copy(initial_deck1),
                                               copy(initial_deck2),
                                               recursive)

    if p1_wins:
        w = final_deck1
    else:
        w = final_deck2

    print(w)
    print(len(w))

    w.reverse()
    score = 0
    for i, c in enumerate(w):
        score += (i + 1)*c
    print(score)
    print()
