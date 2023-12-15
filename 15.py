from collections import defaultdict

def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

test_string = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

### Part 1 ###

def hash(a_str):
    current = 0
    for i in a_str:
        # first update the current with the ascii value of i
        current += ord(i)
        current = (current * 17) % 256

    return current

result = 0
for a in read_input('15')[0].split(','):
    result += hash(a)

print("Answer to Part 1:", result)

### Part 2 ###

# initialize the dictionary with a dict as the default value
boxes = defaultdict(dict)

for a in read_input('15')[0].split(','):
    if '=' in a:
        label = a.split('=')[0]
        focal_length = int(a.split('=')[1])
        box = hash(label)

        # lookup the label in the corresponding box, and update the focal length
        boxes[box][label] = focal_length

    else:
        label = a.split('-')[0]
        box = hash(label)

        # lookup the label in the corresponding box, and remove the label
        if label in boxes[box]:
            boxes[box].pop(label)

sum_all = 0
for box in boxes:
    keys = list(boxes[box].keys())

    for key, value in boxes[box].items():
        order = keys.index(key) + 1
        sum_all += (box+1) * order * value

print("Answer to Part 2:", sum_all)	
