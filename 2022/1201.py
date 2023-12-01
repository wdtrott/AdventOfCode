with open('/Users/wtrott/Downloads/1201input.txt') as file:
    data = [line.strip() for line in file]
    
iter = 1
elves = {1: []}
for line in data:
    if line:
        elves[iter].append(int(line))
    else:
        iter += 1
        elves[iter] = []

sort_cals = dict(sorted({elf: sum(calories) for elf, calories in elves.items()}.items(), key=lambda item: item[1]))

print(f"Max calories: {sort_cals[list(sort_cals.keys())[-1]]}")
print(f"Total for top 3 calories: {sum([sort_cals[key] for key in list(sort_cals.keys())[-3:]])}")
