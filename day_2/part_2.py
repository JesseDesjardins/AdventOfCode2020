lst = []
with open('input.txt', 'r') as infile:
    lst = [line.rstrip('\n') for line in infile]

solution = 0

for entry in lst:
    char_count = 0
    policy_full, password = entry.split(':')
    password = password.strip()
    policy_pos, policy_char = policy_full.split(' ')
    policy_pos_1, policy_pos_2 = policy_pos.split('-')

    if (password[int(policy_pos_1)-1] == policy_char or password[int(policy_pos_2)-1] == policy_char):
        if password[int(policy_pos_1)-1] != password[int(policy_pos_2)-1]: solution += 1

print(solution)