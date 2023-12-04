input = {}
with open('input.txt', 'r') as file:
  for line in file.read().splitlines():
    card, values = line.split(':', 1)
    input[int(card.split(' ')[-1])] = {'winning_num': set(values.split('|')[0].strip().replace('  ', ' ').split(' ')), 'picks': values.split('|')[1].strip().replace('  ', ' ').split(' ')}

wins = {card: 0 for card in input.keys()}
for card, numbers in input.items():
  correct = len(numbers['winning_num'].intersection(numbers['picks']))
  if correct:
    wins[card] = correct
print(sum([int(2 ** (value - 1)) for value in wins.values()]))

total_cards = {card: 1 for card in input.keys()}
for iter in range(1, len(input) + 1):
  cards = total_cards[iter]
  card_win = wins[iter]
  for win in range(1, card_win + 1):
    total_cards[iter + win] += cards

print(sum(total_cards.values()))
