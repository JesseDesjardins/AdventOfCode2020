lst = []
with open('input.txt', 'r') as infile:
    lst = [line.rstrip('\n') for line in infile]

tree_count = 0
traversed = False
horizontal_index = 0
vertical_index = 0

while not traversed:
    # 3 to the right
    horizontal_index = (horizontal_index + 3) % len(lst[vertical_index])
    # 1 down
    vertical_index += 1
    if lst[vertical_index][horizontal_index] == '#':
        tree_count += 1
    if vertical_index == len(lst) - 1:
        traversed = True

print(tree_count)