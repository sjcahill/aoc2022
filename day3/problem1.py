from string import ascii_letters

# define our char to int map
charmap = {k: v for k, v in zip(ascii_letters, range(1, 53))}

# define our priority calculation function for a single rucksack/line of text
def priority_calc(line: str) -> int:
    midpt = len(line) // 2
    first_ruck, second_ruck = line[:midpt], line[midpt:]
    common_char = set(first_ruck).intersection(set(second_ruck))
    return charmap[common_char.pop()]


# variable to hold the sum of priorities
total_priority = 0
with open("rucksack.txt", "r") as f:
    for line in f:
        total_priority += priority_calc(line.strip())

print(total_priority)
