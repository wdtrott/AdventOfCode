with open('/Users/wtrott/Downloads/input1202.txt') as file:
    data = [line.strip().split(' ') for line in file]

num_map = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
total_score = 0
for line in data:
    total_score += num_map[line[1]]
    calc = (num_map[line[1]] - num_map[line[0]]) % 3
    if calc == 1:
        total_score += 6
    elif calc == 0:
        total_score += 3
        
print(f"Total Score with the strategy guide: {total_score}")

second_strategy = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
second_score = 0
for line in data:
    result = second_strategy[line[1]]
    opp_tactic = second_strategy[line[0]]
    second_score += result
    if result == 3:
        second_score += opp_tactic
    elif result == 6:
        win_calc = (opp_tactic - 2) % 3
        if win_calc != 0:
            second_score += win_calc
        else:
            second_score += 3
    else:
        lose_calc = (opp_tactic - 1) % 3
        if lose_calc != 0:
            second_score += (opp_tactic - 1) % 3
        else:
            second_score += 3
            
print(f"Total score with corrected strategy: {second_score}")