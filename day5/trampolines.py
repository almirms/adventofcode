import os
import input_file


def jump(current_position, jumps):
    jump_size = int(jumps[current_position])
    jumps[current_position] = int(jumps[current_position]) + 1

    current_position += jump_size

    return current_position, jumps


def jump_part2(current_position, jumps):
    jump_size = int(jumps[current_position])

    if jump_size >= 3:
        jumps[current_position] = int(jumps[current_position]) - 1
    else:
        jumps[current_position] = int(jumps[current_position]) + 1

    current_position += jump_size

    return current_position, jumps


diretorio = os.path.dirname(os.path.abspath(__file__))
input_string = input_file.read_lines(diretorio)

jumps = list(input_string)

jumps = [s.strip() for s in jumps]

jumps_part1 = jumps[:]
jumps_part2 = jumps[:]

jumps_size = len(jumps)

current_position = 0
iterations = 0

while current_position < jumps_size:
    iterations += 1
    current_position, jumps_part1 = jump(current_position, jumps_part1)

print(iterations)

current_position = 0
iterations = 0
while current_position < jumps_size:
    iterations += 1
    current_position, jumps_part2 = jump_part2(current_position, jumps_part2)

print(iterations)


