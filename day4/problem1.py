# range comparison function
# for simplicity, function isn't commutative and so we will check both arg sequences


def get_range(line: str) -> tuple:
    r1, r2 = line.strip().split(",")
    return (r1, r2)


def range_overlap(ranges: tuple) -> int:
    r1, r2 = ranges[0], ranges[1]
    r1l, r1r = r1.split("-")
    r2l, r2r = r2.split("-")
    if (int(r2l) >= int(r1l)) and (int(r2r) <= int(r1r)):
        return 1
    return 0


overlaps = 0
with open("clean.txt", "r") as f:
    for line in f:
        ranges = get_range(line)
        if range_overlap(ranges) or range_overlap(ranges[::-1]):
            overlaps += 1


print(overlaps)
