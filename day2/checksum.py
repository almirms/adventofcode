import os
from itertools import combinations_with_replacement, permutations

import input_file

diretorio = os.path.dirname(os.path.abspath(__file__))
input_string = input_file.read_lines(diretorio)


def find_divisibles(input_list):
    for combination in permutations(input_list, 2):
        if combination[0] % combination[1] == 0:
            return combination[0] / combination[1]


result = 0

for line in input_string:
    numbers_list = line.split("\t")
    numbers_list = list(map(int, numbers_list))
    max_value = max(numbers_list)
    min_value = min(numbers_list)

    result = result + max_value - min_value

print(result)

result_part2 = 0

for line in input_string:
    numbers_list = line.split("\t")
    numbers_list = list(map(int, numbers_list))

    result_part2 = result_part2 + find_divisibles(numbers_list)

print(result_part2)
