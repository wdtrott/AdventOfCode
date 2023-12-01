with open('input.txt', 'r') as file:
    input = file.readlines()

acc = 0
for line in input:
  digits = [value for value in line if value.isdigit()]
  if digits:
    acc += int(digits[0] + digits[-1])
print(acc)

map = {
'one':'1',
'two':'2',
'three':'3',
'four':'4',
'five':'5',
'six':'6',
'seven':'7',
'eight':'8',
'nine':'9'
}
acc = 0
for line in input:
  temp = []
  for idx, val in enumerate(line):
    if val.isdigit():
      temp.append(val)
    else:
      for key, value in map.items():
        if line[idx:].startswith(key):
          temp.append(value)
  if temp:
    acc += int(temp[0] + temp[-1])
print(acc)
