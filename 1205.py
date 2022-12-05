import copy
import re

class crane_problem():
    def __init__(self):
        with open('/Users/wtrott/Downloads/input1205.txt') as file:
            data = [line.strip('\n') for line in file if line.strip('\n')]
        self.raw_initial_state = [line for line in data if 'move' not in line]
        self._encode_initial_state([line for line in data if 'move' not in line])
        self._parse_moves([line for line in data if 'move' in line])
        
    def _encode_initial_state(self, initial_state):
        self.initial_state = {}
        for state in initial_state:
            for ind in range(0, 9):
                box = state[1 + 4 * ind]
                # Don't need to append if there isn't anything there or we have the index row
                if box == ' ' or box.isdigit():
                    continue
                if self.initial_state.get(ind + 1, False):
                    self.initial_state[ind + 1].insert(0, box)
                else:
                    self.initial_state[ind + 1] = [box]
        
    
    def _parse_moves(self, moves):
        self.moves = [[int(move_val) for move_val in re.findall(r"\d+", move)] for move in moves ]
        
    def move_boxes(self):
        movements = copy.deepcopy(self.initial_state)
        for plan in self.moves:
            num_to_move = plan[0]
            move_from = plan[1]
            move_to = plan[2]
            for move in range(1, num_to_move + 1):
                removed_box = movements[move_from].pop(-1)
                movements[move_to].append(removed_box)
        output = dict(sorted(movements.items()))
        print("Final state:")
        for stack, boxes in output.items():
            print(f"{stack}: {boxes[-1]}")
    
    def move_boxes_9001(self):
        movements = copy.deepcopy(self.initial_state)
        for plan in self.moves:
            num_to_move = plan[0]
            move_from = plan[1]
            move_to = plan[2]
            
            # Split the box on the number to move
            remaining_boxes = movements[move_from][:-1 * num_to_move]
            moving_boxes = movements[move_from][-1 * num_to_move:]
            movements[move_from] = remaining_boxes
            movements[move_to].extend(moving_boxes)
            
        output = dict(sorted(movements.items()))
        print("Final state with 9001 Logic:")
        for stack, boxes in output.items():
            print(f"{stack}: {boxes[-1]}")
            
box_mover = crane_problem()
box_mover.move_boxes()
box_mover.move_boxes_9001()
