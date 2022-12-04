# range comparison function
# for simplicity, function isn't commutative and so we will check both arg sequences


def get_range(line: str) -> tuple:
    r1, r2 = line.strip().split(",")
    return (r1, r2)


# Ranges don't overlap when one of them starts after the other ends
# x1 > y2 || y1 > x2
# So they do overlap if this is not true
# x1 <= y2 && y1 <= x2
def range_overlap(ranges: tuple) -> int:
    r1, r2 = ranges[0], ranges[1]
    r1l, r1r = r1.split("-")
    r2l, r2r = r2.split("-")
    if int(r1l) <= int(r2r) and int(r2l) <= int(r1r):
        return 1
    return 0


overlaps = 0
with open("clean.txt", "r") as f:
    for line in f:
        ranges = get_range(line)
        if range_overlap(ranges):
            overlaps += 1


print(overlaps)
