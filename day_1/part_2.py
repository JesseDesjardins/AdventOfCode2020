import itertools

lst = []
with open('input.txt', 'r') as infile:
    lst = [line.rstrip('\n') for line in infile]

solution = None
for x, y, z in itertools.combinations(lst, 3):
    if (int(x) + int(y) + int(z)) == 2020:
        print('{} + {} + {} = {}'.format(x, y, z, int(x) + int(y) + int(z))) 
        solution = int(x) * int(y) * int(z)
        break
print(solution)
