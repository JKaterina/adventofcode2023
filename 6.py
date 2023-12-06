# open the text file inputs/1.txt
def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

data = read_input('6')

times = [int(x) for x in data[0].split(': ')[1].split(' ') if x != '']
distances = [int(x) for x in data[1].split(': ')[1].split(' ') if x != '']

# create tuples of (time, distance)
pairs = [(times[i], distances[i]) for i in range(len(times))]

### Part 1 ###

def get_distance_travelled(pair):
    # exclude 0 and max value as it never makes sense
    # start the counter
    counter = 0
    for i in range(1, pair[0]):
        # distance travelled with the current power
        distance = (pair[0] - i) * i
        if distance > pair[1]:
            counter += 1

    return counter

result = 1
for pair in pairs:
    result *= get_distance_travelled(pair)

print("Answer to part 1: ", result)

