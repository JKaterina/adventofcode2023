import numpy as np
from collections import defaultdict

def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

grid = np.array([list(row) for row in read_input('21')])
# find the location of S
s_x, s_y = np.where(grid == 'S')

# initialize the step_dict step 0 with the location of S
step_dict = defaultdict(list)
step_dict[0].append((s_x[0], s_y[0]))

def check_around(x, y, step_list):
    # check the 4 directions
    if grid[x-1, y] != '#':
        step_list.append(((x-1), y))
    if grid[x+1, y] != '#':
        step_list.append(((x+1), y))
    if grid[x, y-1] != '#':
        step_list.append((x, (y-1)))
    if grid[x, y+1] != '#':
        step_list.append((x, (y+1)))

benchmark = 64

current_step = 1
while current_step < (benchmark + 1):
    previous_step = current_step - 1
    for i in step_dict[previous_step]:
        # check around each element in the previous step and update the step_dict for the current step
        check_around(i[0], i[1], step_dict[current_step])
        # remove duplicates
        step_dict[current_step] = list(set(step_dict[current_step]))
    current_step += 1

print("Answer to Part 1:", len(step_dict[benchmark]))