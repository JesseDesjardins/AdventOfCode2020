import itertools

lst = []
with open('input.txt', 'r') as infile:
    lst = [line.rstrip('\n') for line in infile]

solution = None
for x, y in itertools.combinations(lst, 2):
    if (int(x) + int(y)) == 2020:
        print('{} + {} = {}'.format(x, y, int(x) + int(y))) 
        solution = int(x) * int(y)
        break
print(solution)
