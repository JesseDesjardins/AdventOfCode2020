lst = []
with open('input.txt', 'r') as infile:
    lst = [line.rstrip('\n') for line in infile]

solution = 0

for entry in lst:
    char_count = 0
    policy_full, password = entry.split(':')
    password = password.strip()
    policy_count, policy_char = policy_full.split(' ')
    policy_count_min, policy_count_max = policy_count.split('-')
    for char in password:
        if char == policy_char:
            char_count += 1
    if char_count in range(int(policy_count_min), int(policy_count_max)+1): solution += 1

print(solution)