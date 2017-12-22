import os.path
import numpy as np
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 21 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.strip('\n'))

test = ['../.# => ##./#../...',
        '.#./..#/### => #..#/..../..../#..#']

starting_state = [[0,1,0], [0, 0, 1], [1, 1, 1]]

def rotate(block):
    block_set = set()
    block_set.add(tuple(tuple(x) for x in block))
    mirror_y = [list(reversed(x)) for x in block]
    block_set.add(tuple(tuple(x) for x in mirror_y))
    mirror_x = list(reversed(block))
    block_set.add(tuple(tuple(x) for x in mirror_x))
    clockwise = np.rot90(block, 1)
    block_set.add(tuple(tuple(x) for x in clockwise))
    clockwise_y = [list(reversed(x)) for x in clockwise]
    block_set.add(tuple(tuple(x) for x in clockwise_y))
    clockwise_x = list(reversed(clockwise))
    block_set.add(tuple(tuple(x) for x in clockwise_x))
    one_eight = np.rot90(block, 2)
    block_set.add(tuple(tuple(x) for x in one_eight))
    one_eight_y = [list(reversed(x)) for x in one_eight]
    block_set.add(tuple(tuple(x) for x in one_eight_y))
    one_eight_x = list(reversed(one_eight))
    block_set.add(tuple(tuple(x) for x in one_eight_x))
    counter = np.rot90(block, 3)
    block_set.add(tuple(tuple(x) for x in counter))
    counter_y = [list(reversed(x)) for x in counter]
    block_set.add(tuple(tuple(x) for x in counter_y))
    counter_x = list(reversed(counter))
    block_set.add(tuple(tuple(x) for x in counter_x))
    return block_set

def format_input(puzzle):
    rules = dict()
    for line in puzzle:
        line = line.split()
        block = []
        block_line = []
        for i in line[0]:
            if i == '.':
                block_line.append(0)
            elif i == '#':
                block_line.append(1)
            elif i == '/':
                block.append(block_line)
                block_line = []
        block.append(block_line)
        block_set = rotate(block)
        output = []
        output_line = []
        for i in line[2]:
            if i == '.':
                output_line.append(0)
            elif i == '#':
                output_line.append(1)
            elif i == '/':
                output.append(output_line)
                output_line = []
        output.append(output_line)
        for block in block_set:
            rules[block] = output
    return rules

def one_iteration(picture, rules):
    if len(picture) % 2 == 0:
        block_size = 2
    else:
        block_size = 3
    new_picture = []
    for i in range(0, len(picture), block_size):
        next_rows = []
        for j in range(block_size + 1):
            next_rows.append([])
        for j in range(0, len(picture), block_size):
            rows = picture[i:i + block_size]
            block = []
            for row in rows:
                block.append(row[j:j + block_size])
            output = rules[tuple(tuple(x) for x in block)]
            for k in range(block_size + 1):
                next_rows[k].extend(output[k])
        new_picture.extend(next_rows)
    return new_picture

def multiple_iterations(puzzle, iterations):
    state = starting_state
    rules = format_input(puzzle)
    for i in range(iterations):
        state = one_iteration(state, rules)
    pixels = 0
    for row in state:
        pixels += sum(row)
    return pixels

# print(multiple_iterations(test, 2))
# print(multiple_iterations(puzzle, 5))
print(multiple_iterations(puzzle, 18))
