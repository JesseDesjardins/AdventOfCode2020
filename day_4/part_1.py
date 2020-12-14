import re

passports = []
with open('input.txt', 'r') as infile:
    passport = ''
    for line in infile:
        if line.rstrip('\n') != '': 
            passport += line
        else: 
            passports.append(passport)
            passport = ''

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_keys = ['cid']

valid_count = 0

for passport in passports:
    fields = [item for item in re.split(r"[\s|\n]+", passport)]
    fields.remove('')
    print(fields)
    keys = [splits[0] for splits in (field.split(':') for field in fields)]
    print(keys)
    print('')
    if len(set(keys).intersection(required_keys)) >= 7: valid_count += 1

print(valid_count)
print(len(passports))