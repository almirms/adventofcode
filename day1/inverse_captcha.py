import os

import input_file


def get_next_element( input_string, idx ):
    if idx + 1 >= len(input_string):
        return input_string[0]
    else:
        return input_string[idx + 1]


def get_next_element_part2( input_string, idx ):
    if idx + 1 >= len(input_string):
        return input_string[0]
    else:
        return input_string[idx + 1]


diretorio = os.path.dirname(os.path.abspath(__file__))
input_string = input_file.read_lines(diretorio)[0]

result_part1 = 0

for idx, val in enumerate(input_string):

    next_element = get_next_element(input_string, idx)

    if next_element == val:
        result = result + int(val)

print(result_part1)

result_part2 = 0

for idx, val in enumerate(input_string):

    next_element = get_next_element_part2(input_string, idx)

    if next_element == val:
        result = result + int(val)

print(result_part1)
