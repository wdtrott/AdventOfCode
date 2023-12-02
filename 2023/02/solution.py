import re

with open('input.txt', 'r') as file:
  input = {line.split(':')[0]:line.split(':')[-1]  for line in file.readlines()}

acc = 0
for game, values in input.items():
  game_number = game.split(' ')[-1]
  if game_number == '\n':
    continue
  valid = True
  temp = values.lower().replace('\n', '').replace(' ', '').split(';')
  for pull in temp:
    if 'red' in pull:
      if [int(num.replace('red', '')) for num in re.findall(r'\d+red', pull)][0] > 12:
        valid = False
    if 'green' in pull:
      if [int(num.replace('green', '')) for num in re.findall(r'\d+green', pull)][0] > 13:
        valid = False
    if 'blue' in pull:
      if [int(num.replace('blue', '')) for num in re.findall(r'\d+blue', pull)][0] > 14:
        valid = False
  if valid:
    acc += int(game_number)

print(acc)

acc = 0
for _, values in input.items():
  temp = values.lower().replace('\n', '').replace(' ', '').split(';')

  min_green = 0 
  min_blue = 0 
  min_red = 0 

  for pull in temp:
    if 'red' in pull:
      red_val = [int(num.replace('red', '')) for num in re.findall(r'\d+red', pull)][0]
      if red_val > min_red:
        min_red = red_val
    if 'green' in pull:
      green_val = [int(num.replace('green', '')) for num in re.findall(r'\d+green', pull)][0]
      if green_val > min_green:
        min_green = green_val
    if 'blue' in pull:
      blue_val = [int(num.replace('blue', '')) for num in re.findall(r'\d+blue', pull)][0]
      if blue_val > min_blue:
        min_blue = blue_val
    print({'red': min_red, 'blue': min_blue, 'green': min_green}) 
  acc += min_red * min_blue * min_green

print(acc)
