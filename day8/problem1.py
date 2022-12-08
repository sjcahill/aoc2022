# Naive attempt
# If a tree is visible from top, left, bottom OR right. Then it is visible.
# Can look from the outside for each row/column from both directions to find all of our visible trees
# Want to generate an array of 0s and change them to ones as we identify visible trees.
# Remember a tree of equal height to one in front of it is NOT visible

trees: list = []

with open("input.txt", "r") as f:
    for line in f:
        trees.append([])
        for char in line.strip():
            trees[-1].append(int(char))

vis = [[0] * len(trees[0]) for _ in range(len(trees))]

# Now I have trees and vis "matrices" and need to see which trees I can see

for i in range(99):
    cur_max = -1
    for idx, height in enumerate(trees[i]):
        if height > cur_max:
            cur_max = height
            vis[i][idx] = 1
        if cur_max == 9:
            break

    cur_max = -1
    for idx, height in enumerate(trees[i][::-1]):
        if height > cur_max:
            cur_max = height
            vis[i][-idx-1] = 1
        if cur_max == 9:
            break

print(sum([sum(s) for s in vis]))


#     cur_max = -1
#     for idx, height in enumerate(trees[i][::-1])


# def vis_finder(tree_row: list, vis_row: list):
#     cur_max = -1
#     for i, height in enumerate(tree_row):
#         if height > cur_max:
#             cur_max = height
#             vis_row[i] = 1
#         if height == 9:
#             break


# for i in range(99):
#     vis_finder(trees[i], vis[i])
#     vis_finder(trees[-i], vis[-i])

#     tree_tuples = list(zip(*trees))
#     tree_cols = [list(sublist) for sublist in tree_tuples]

#     vis_tuples = list(zip(*vis))
#     vis_cols = [list(sublist) for sublist in vis_tuples]
#     vis_finder(tree_cols[i], vis_cols[i])
#     vis_finder(tree_cols[i][::-1], vis_cols[i][::-1])

# print(sum([sum(v) for v in vis]))

