with open('/Users/wtrott/Downloads/input1204.txt') as file:
    data = [
        [
            [int(assignment) for assignment in line.strip('\n').split(',')[0].split('-')]
            , [int(assignment) for assignment in line.strip('\n').split(',')[1].split('-')]
        ]
            for line in file]

def build_ranges(assignment_lists):
    return set(range(assignments[0][0], assignments[0][1] + 1)), set(range(assignments[1][0], assignments[1][1] + 1))
    
assignment_contained = 0
for assignments in data:
    first_assignments, second_assignments = build_ranges(assignments)
    if len(first_assignments.intersection(second_assignments)) == min(len(first_assignments), len(second_assignments)):
        assignment_contained += 1
print(f"The number of assignments with a full overlap is {assignment_contained}")

overlaps = 0
for assignments in data:
    first_assignments, second_assignments = build_ranges(assignments)
    if first_assignments.intersection(second_assignments):
        overlaps += 1
print(f"The number of assignments with overlaps is {overlaps}")
