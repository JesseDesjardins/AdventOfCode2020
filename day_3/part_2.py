import math

lst = []
with open('input.txt', 'r') as infile:
    lst = [line.rstrip('\n') for line in infile]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []

for slope in slopes:
    tree_count = 0
    traversed = False
    horizontal_index = 0
    vertical_index = 0

    while not traversed:
        # 3 to the right
        horizontal_index = (horizontal_index + slope[0]) % len(lst[vertical_index])
        # 1 down
        vertical_index += slope[1]
        if vertical_index < len(lst) and lst[vertical_index][horizontal_index] == '#':
            tree_count += 1
        if vertical_index >= len(lst) - 1:
            traversed = True
            trees.append(tree_count)

print(math.prod(trees))