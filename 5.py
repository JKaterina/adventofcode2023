import re

# open the text file inputs/1.txt
def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

### Part 1 ###
data = read_input('5')

def get_maps():
    '''Get the maps as the list of lists'''
    maps = []
    current_map = []
    for line in data[1:]:
        if line == '':
            if current_map:
                maps.append(current_map)
                current_map = []
        else:
            current_map.append(line)

    if current_map:
        maps.append(current_map)

    return maps

seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]
maps = get_maps()

def get_value_based_on_source_seed(source):

    source_value = source
    for m in maps:
        values = m[1:]

        for i in values:
            i = [int(x) for x in i.split(' ')]
            source_interval = range(i[1], i[1] + i[2])

            # update source value for the next map
            if source_value in source_interval:
                # find the distance from the start of the interval
                distance = source_value - i[1]
                # new source value is the destination start + the distance
                source_value = i[0] + distance
                # source found, move to the next map
                break
            else:
                # keep the source value, move to the next map
                pass

    return source_value

final_values = [get_value_based_on_source_seed(seed) for seed in seeds]
print("Answer to part 1: ", min(final_values))

### Part 2 ###
