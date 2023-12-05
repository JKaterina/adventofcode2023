import re

# open the text file inputs/1.txt
def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

### Part 1 ###
# benchmark dictionary
benchmarks = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum_of_game_indx = 0
for line in read_input('2'):    
    # separate the sets
    sets = line.split(';')
    # game index to be summed
    game_index = int(re.findall(r'Game (\d+)', line)[0])
    # number of correct conditions
    correct_conditions = 1
    for set in sets:
        # find a pattern digit-space-color
        for color in benchmarks.keys():
            pattern = fr'(\d+) {color}'
            # find all matches
            matches = re.findall(pattern, set)
            sum_of_matches = sum([int(x) for x in matches])
            # sum the matches and add to correct_conditions if the sum is less than the benchmark
            if sum([int(x) for x in matches]) <= benchmarks[color]:
                correct_conditions *= 1
            else:
                correct_conditions *= 0

    # if conditions for all colors are met, add the game index to the sum
    if correct_conditions == 1:
        sum_of_game_indx += game_index

print("Answer to part 1: ", sum_of_game_indx)

### Part 2 ###
final_sum = 0
for line in read_input('2'):    

    multiplication_of_max_values = 1
    # find the maximum value per color and multiply them
    for color in benchmarks.keys():
        pattern = fr'(\d+) {color}'
        # find all matches per color and translate to integers	
        max_value = max([int(x) for x in re.findall(pattern, line)])
        multiplication_of_max_values *= max_value
    
    final_sum += multiplication_of_max_values

print("Answer to part 2: ", final_sum)