import re

symbols = {}
digits = {}
gears = {}

with open('input.txt', 'r') as file:
  for row, line in enumerate(file.read().splitlines()):
    symbols[row] = []
    digits[row] = {}
    gears[row] = []

    for match in re.finditer(r'\d+', line):
      digits[row][match.span()] = int(match.group())

    for match in re.finditer(r'[^\d.]', line):
      symbols[row].append(match.start())
    for match in re.finditer(r'\*', line):
      gears[row].append(match.start())

acc = 0
for row, input in digits.items():
  previous_sym = symbols.get(row - 1, [])
  current_sym = symbols.get(row,[]) 
  next_sym = symbols.get(row + 1, [])
  possible_symbols = previous_sym + current_sym + next_sym
 
  for span, number in input.items():
    window = set(range(span[0] - 1, span[1] + 1))
    if window.intersection(possible_symbols):
      acc += number
print(acc)

acc = 0
for row, gear in gears.items():
  for position in gear:
    position_filter = set(range(position - 1, position + 2))
    previous_ratio = [number for span, number in digits.get(row - 1, {}).items() 
        if position_filter.intersection(range(span[0], span[1]))]
    current_ratio = [number for span, number in digits.get(row, {}).items() 
        if position_filter.intersection(range(span[0], span[1]))]
    next_ratio = [number for span, number in digits.get(row + 1, {}).items() 
        if position_filter.intersection(range(span[0], span[1]))]
    overlap = previous_ratio + current_ratio + next_ratio
    if len(overlap) == 2:
      acc += overlap[0] * overlap[1]

print(acc)
