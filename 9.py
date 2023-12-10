import numpy as np

def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

data = []
for line in read_input('9'):
    int_list = [int(i) for i in line.split()]
    data.append(int_list)

### Part 1 ###
def first_part(int_list):
    pattern = np.array(int_list, dtype=int).reshape(1, -1)

    final_number = 0

    while not np.all(np.diff(pattern) == 0):

        final_number += pattern[-1, -1]
        pattern = np.diff(pattern)

    else:
        # still add the last number
        final_number += pattern[-1, -1]

    return final_number

result_1 = 0
for i in data:
    result_1 += first_part(i)
print("Answer to part 1:", result_1)

### Part 2 ###
def second_part(int_list):
    pattern = np.array(int_list, dtype=int).reshape(1, -1)

    final_number = 0 
    sign = 1

    while not np.all(np.diff(pattern) == 0):

        final_number += pattern[0, 0] * sign
        sign *= -1
        pattern = np.diff(pattern)

    else:
        # still add the first number
        final_number += pattern[0, 0] * sign
        sign *= -1

    return final_number

result_2 = 0
for i in data:
    result_2 += second_part(i)
    
print("Answer to part 2:", result_2)

