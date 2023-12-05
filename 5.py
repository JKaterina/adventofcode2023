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

# every two seeds form a range
# split seeds into ranges
# ranges = []
# for i in range(0, len(seeds), 2):
#     ranges.append([seeds[i], seeds[i] + seeds[i + 1]])

# all_values = []
# for r in ranges:
#     r = range(r[0], r[1])
#     for i in r:
#         all_values.append(get_value_based_on_source_seed(i))

from functools import reduce

seeds, *mappings = open(r'C:\Users\uljan\Documents\adventofcode2023\inputs\5.txt').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))


def lookup(inputs, mapping):
    outputs = []

    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                if src <= start < src+len:
                    len -= max(start-src, len-length)
                    outputs.append((start-src+dst, len))
                    start += len
                    length -= len
                    break
            else:
                outputs.append((start, length))
                break

    return outputs


print(*[min(reduce(lookup, mappings, s))[0] for s in [
    zip(seeds, [1] * len(seeds)),
    zip(seeds[0::2], seeds[1::2])]])