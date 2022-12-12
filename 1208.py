with open('/Users/wtrott/Downloads/input1208.txt') as file:
    data = {row: {column: int(value) for column, value in enumerate(line.replace('\n', '' ))} for row, line in enumerate(file)}
total_rows = max(data.keys()) + 1
total_cols = max(data[0].keys()) + 1

def check_height(x_pos: int, y_pos: int, direction: str, grid):
    if direction == 'horizontal':
        height_list = [tree_height for tree_height in grid[x_pos].values()]
        height = height_list[y_pos]
        comparison_index = y_pos
    elif direction == 'vertical':
        height_list = [row[y_pos] for row in grid.values()]
        height = height_list[x_pos]
        comparison_index = x_pos
    lead_trees = height_list[:comparison_index]
    lag_trees = height_list[comparison_index + 1:]
    return height > min(max(lead_trees), max(lag_trees))

total_viewable_trees = 2 * (total_rows + total_cols - 2)
viewable_trees = []
for row in data.keys():
    if row == 0 or row == total_rows - 1:
        continue
    for column in data[row].keys():
        if column == 0 or column == total_cols - 1:
            continue
        if check_height(row, column, 'horizontal', data) or check_height(row, column, 'vertical', data):
            total_viewable_trees += 1
            viewable_trees.append((row, column))
print(f"Total viewable trees: {total_viewable_trees}")

def scenic_score(x_pos: int, y_pos: int, grid):
    horizontal = [height for height in grid[x_pos].values()]
    vertical = [height[y_pos] for height in grid.values()]
    height = grid[x_pos][y_pos]
    
    left_score = calc_score(horizontal[:y_pos][::-1], height)
    right_score = calc_score(horizontal[y_pos+1:], height)
    up_score = calc_score(vertical[:x_pos][::-1], height)
    down_score = calc_score(vertical[x_pos+1 :], height)
    return left_score * right_score * up_score * down_score

def calc_score(height_list, height):
    score = 0 
    if height_list:
        for tree in height_list:
            if height <= tree:
                return score + 1
            else:
                score += 1
        return score
    else: 
        return score

max_score = 0
for row in data.keys():
    if row == 0 or row == total_rows - 1:
        continue
    for column in data[row].keys():
        if column == 0 or column == total_cols - 1:
            continue
        max_score = max(scenic_score(row, column, data), max_score)

print(f"Highest scenic score: {max_score}")
