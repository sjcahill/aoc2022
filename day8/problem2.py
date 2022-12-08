def check_left(trees, i, j):

    tree_height = trees[i][j]
    view_distance = 0

    if j == 0:
        return 0

    while j >= 1:
        if trees[i][j - 1] < tree_height:
            view_distance += 1
            j -= 1
            if j == 0:
                return view_distance
        else:
            break

    return view_distance + 1


def check_right(trees, i, j):

    tree_height = trees[i][j]
    view_distance = 0

    if j == len(trees) - 1:
        return 0

    while j <= len(trees) - 2:
        if trees[i][j + 1] < tree_height:
            view_distance += 1
            j += 1
            if j == len(trees) - 1:
                return view_distance
        else:
            break

    return view_distance + 1


def check_up(trees, i, j):

    tree_height = trees[i][j]
    view_distance = 0

    if i == 0:
        return 0

    while i >= 1:
        if trees[i - 1][j] < tree_height:
            view_distance += 1
            i -= 1
            if i == 0:
                return view_distance
        else:
            break

    return view_distance + 1


def check_down(trees, i, j):

    tree_height = trees[i][j]
    view_distance = 0

    if i == len(trees) - 1:
        return 0

    while i <= len(trees) - 2:
        if trees[i + 1][j] < tree_height:
            view_distance += 1
            i += 1
            if i == len(trees) - 1:
                return view_distance
        else:
            break

    return view_distance + 1


def get_max_view_distance(trees):
    max_distance = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            l = check_left(trees, i, j)
            r = check_right(trees, i, j)
            d = check_down(trees, i, j)
            u = check_up(trees, i, j)

            max_distance = max(max_distance, l * r * d * u)

    return max_distance


trees: list = []

with open("input.txt", "r") as f:
    for line in f:
        trees.append([])
        for char in line.strip():
            trees[-1].append(int(char))


md = get_max_view_distance(trees)
print(md)

print(len(trees))
print(len(trees[0]))
