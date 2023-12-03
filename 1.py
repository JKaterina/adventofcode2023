# open the text file inputs/1.txt
def read_input(puzzle):
    with open(f'inputs/{puzzle}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

### Part 1 ###

def construct_integers():
    sum_of_digits = 0
    for i in read_input('1'):
        # split string into list of characters
        chars = list(i)
        # check if a character is a digit
        first_digit = next((x for x in chars if x.isdigit()), None)
        last_digit = next((x for x in chars[::-1] if x.isdigit()), None)

        final_digit = int(first_digit + last_digit)
        sum_of_digits += final_digit

    return sum_of_digits

### Part 2 ###

# define a dictionary with the follwing format: {one: 1, two: 2, ...}
word_to_number = {
    'zero' : 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def replace_number_with_word(string):
    '''Replace all numbers in a string with their corresponding word
    Example: "two1nine" -> "twoonenine" '''	
    for word, number in word_to_number.items():
        string = string.replace(str(number), word)
    return string

def find_substrings_with_digits(string):
    ''' Find all substrings in a string that contain digits
    Example: "eightwothree" -> ["eight", "two", "three"] 
    The function returns the substrings in the order they appear in the string 
    and translates them to their corresponding number'''
    substrings_with_indices = []

    for word in word_to_number.keys():
        index = string.find(word)
        while index != -1:
            substrings_with_indices.append((word, index))
            index = string.find(word, index + 1)

    # sort the substrings based on their indices
    substrings_with_indices.sort(key=lambda x: x[1])

    # extract the translated numbers from the sorted substrings
    substrings_translated = [word_to_number[word] for word, _ in substrings_with_indices]
    return substrings_translated

def construct_integers_from_words():
    second_sum_of_digits = 0
    
    for i in read_input('1'):
        # replace numbers with words
        string = replace_number_with_word(i)
        # find all substrings with digits
        substrings = find_substrings_with_digits(string)

        first_digit = substrings[0]
        last_digit = substrings[-1]
        final_digit = first_digit*10 + last_digit

        second_sum_of_digits += final_digit

    return second_sum_of_digits


if __name__ == '__main__':
    
    print("Answer to part 1: {}".format(construct_integers()))
    print("Answer to part 2: {}".format(construct_integers_from_words()))
