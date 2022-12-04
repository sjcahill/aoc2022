from string import ascii_letters
from itertools import islice

# Notes
# Similar problem, but now we want to deal with 3 lines at a time

# define our char to int map
charmap = {k: v for k, v in zip(ascii_letters, range(1, 53))}

# define our priority calculation function for a single rucksack/line of text
def priority_calc(lines: list[str]) -> int:
    elf1, elf2, elf3 = [l.strip() for l in lines]
    common_char = set(elf1).intersection(elf2).intersection(elf3)
    return charmap[common_char.pop()]


# variable to hold the sum of priorities
total_priority = 0
with open("rucksack.txt", "r") as f:
    while True:
        lines = list(islice(f, 3))
        if not lines:
            break
        total_priority += priority_calc(lines)


print(total_priority)
