from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
curr = []

with open("input.txt", "r") as f:
    for line in f:
        match line.split():
            case "$", "cd", "/":
                curr = ["/"]
            case "$", "cd", "..":
                curr.pop()
            case "$", "cd", x:
                curr.append(x + "/")
            case "dir", _:
                pass
            case "$", "ls":
                pass
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)


print(sum(s for s in dirs.values() if s <= 100_000))

print(min(s for s in dirs.values() if s >= dirs["/"] - 40_000_000))
