import numpy as np

# open the text file inputs/1.txt
def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

grid_array = np.array([list(row) for row in read_input('3')])
print(grid_array)

### Part 1 ###
# find symbols
# check all the positions around
# if there is a number, add the number to the list

part_numbers = []

rows, cols = grid_array.shape

for x in range(rows):
    for y in range(cols):
        position = grid_array[x, y]
        if (position.isdigit() == False) & (position != '.'):
            print(f"Symbol {grid_array[x][y]} found at position {x, y}")

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    new_row, new_col = x + di, y + dj
                    try:
                        if grid_array[new_row, new_col].isdigit():
                            print(f"Found number {grid_array[new_row, new_col]} at position {new_row, new_col}")
                            # if the position to the left is a digit, add it to the number
                            # if the position to the right is a digit, add it to the number
                            while grid_array[new_row, new_col - 1].isdigit():
                                new_col -= 1
                                # keep adding the numbers to the left until a non-digit is found

                            final_number = ""
                            while grid_array[new_row, new_col].isdigit():
                                final_number += grid_array[new_row, new_col]
                                new_col += 1

                            # Check positions to the right
                            while grid_array[new_row, new_col + 1].isdigit():
                                final_number += grid_array[new_row, new_col + 1]
                                new_col += 1

                            part_numbers.append(final_number)
                            #break

                    except IndexError:
                        continue

print(part_numbers)