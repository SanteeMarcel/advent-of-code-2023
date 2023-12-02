import re

def capture_digits_and_indices(input_string):
    pattern = re.compile(r'\d')

    matches = pattern.finditer(input_string)

    result = [(match.group(), match.start()) for match in matches]

    return result

def capture_word_and_indices(input_string, word):
    pattern = re.compile(re.escape(word))

    matches = pattern.finditer(input_string)

    result = [(match.group(), match.start()) for match in matches]

    return result

f = open("input.txt", "r")
converter = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

numbers = []

for line in f:
    digits_and_indices = capture_digits_and_indices(line)

    for key in converter.keys():
        digits_and_indices.extend(capture_word_and_indices(line, key))
    
    sorted_list = sorted(digits_and_indices, key=lambda x: x[1])

    first_digit = converter[sorted_list[0][0]] if sorted_list[0][0] in converter else sorted_list[0][0]
    last_digit = converter[sorted_list[-1][0]] if sorted_list[-1][0] in converter else sorted_list[-1][0]

    numbers.append(first_digit + last_digit)

print(sum(map(lambda x: int(x), numbers)))

f.close()
