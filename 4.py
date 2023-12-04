# open the text file inputs/1.txt
def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

### Part 1 ###
total_points = 0
for line in read_input('4'):
    winning_numbers = [int(x) for x in line.split(':')[1].split('|')[0].split(' ') if x != '']
    my_numbers = [int(x) for x in line.split(':')[1].split('|')[1].split(' ') if x != '']

    # find the intersection of two lists
    my_set = [x for x in my_numbers if x in winning_numbers]

    # if the intersection is not empty, the points are calculated as 2^(n-1), where n is the count of matching numbers
    if len(my_set) > 0:
        points = 2 ** (len(my_set) - 1)
        total_points += points

print("Answer to part 1:", total_points)