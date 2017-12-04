import os
from collections import Counter
from itertools import permutations

import input_file


def is_valid(passphrase):
    for key, value in Counter(passphrase).items():
        if value > 1:
            return False
    return True


def is_valid_part2(passphrase):
    for permutation in permutations(passphrase, 2):
        str1_list = list(permutation[0])
        str1_list.sort()
        str2_list = list(permutation[1])
        str2_list.sort()

        if str1_list == str2_list:
            return False

    return True


diretorio = os.path.dirname(os.path.abspath(__file__))
input_string = input_file.ler_linhas(diretorio)

result = 0

for line in input_string:
    line = line.rstrip("\n")
    passphrase = line.split(" ")

    if is_valid(passphrase):
        result += 1

print(result)

result_part2 = 0

for line in input_string:
    line = line.rstrip("\n")
    passphrase = line.split(" ")

    if is_valid(passphrase) and is_valid_part2(passphrase):
        result_part2 += 1

print(result_part2)
