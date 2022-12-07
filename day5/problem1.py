from collections import deque
from itertools import islice

stacks = [deque() for _ in range(0, 9)]

# top of crate is RHS, use pop() to get this thing
with open("crate_stacks.txt", "r") as f:
    for line in f:
        for idx, char in enumerate(line.strip()):
            if char.isalpha():
                stacks[idx // 4].appendleft(char)

with open("moves.txt", "r") as f:
    for line in f:
        moves = [int(n) for n in line.split() if n.isdigit()]
        num_crates, from_stack, to_stack = moves

        crate_queue = []
        for n in range(num_crates):
            cur_crate = stacks[from_stack - 1].pop()
            crate_queue.append(cur_crate)

        stacks[to_stack - 1].extend(crate_queue)


result = "".join([stack[-1] for stack in stacks])
print(result)
