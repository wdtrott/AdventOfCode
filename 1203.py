import string
priority = {letter: string.ascii_lowercase.index(letter) + 1 for letter in string.ascii_lowercase}
priority.update({letter: string.ascii_uppercase.index(letter) + 27 for letter in string.ascii_uppercase})

with open('/Users/wtrott/Downloads/input1203.txt') as file:
    data = [[set(line.strip('\n')[:len(line.strip('\n')) // 2]),set(line.strip('\n')[len(line.strip('\n')) // 2:])] for line in file]

total = 0
for line in data:
    common_item = list(line[0].intersection(line[1]))[0]
    total += priority[common_item]
print(f'Total value: {total}')

badge_total = 0
for iter in range(len(data) // 3):
    first_elf = data[3 * iter][0].union(data[3 * iter][1]) 
    second_elf = data[3 * iter + 1][0].union(data[3 * iter + 1][1]) 
    third_elf = data[3 * iter + 2][0].union(data[3 * iter + 2][1]) 
    common_item = list(first_elf.intersection(second_elf).intersection(third_elf))[0]
    badge_total += priority[common_item]
print(f"Badge priority: {badge_total}")
