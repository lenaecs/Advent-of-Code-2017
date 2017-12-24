import copy
import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 24 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.strip())

test = ['0/2', '2/2', '2/3', '3/4', '3/5', '0/1', '10/1', '9/10']

def clean_puzzle(puzzle):
    puzzle_list = []
    for i in puzzle:
        i = i.split('/')
        i[0], i[1] = int(i[0]), int(i[1])
        puzzle_list.append(i)
    return puzzle_list

def strongest_bridge(puzzle, edge):
    possible_list = []
    for i in range(len(puzzle)):
        if edge in puzzle[i]:
            possible_list.append(i)
    if possible_list == []:
        return 0
    else:
        possible_bridges = []
        for i in possible_list:
            puzzle_copy = copy.deepcopy(puzzle)
            component = puzzle_copy.pop(i)
            component.remove(edge)
            possible_bridges.append(edge + component[0] + strongest_bridge(puzzle_copy, component[0]))
        return max(possible_bridges)

# print(strongest_bridge(clean_puzzle(test), 0))
# print(strongest_bridge(clean_puzzle(puzzle), 0))

def strongest_longest_bridge(puzzle, edge):
    possible_list = []
    for i in range(len(puzzle)):
        if edge in puzzle[i]:
            possible_list.append(i)
    if possible_list == []:
        return 0, 0
    else:
        possible_bridges = []
        for i in possible_list:
            puzzle_copy = copy.deepcopy(puzzle)
            component = puzzle_copy.pop(i)
            component.remove(edge)
            longest = strongest_longest_bridge(puzzle_copy, component[0])
            possible_bridges.append((1 + longest[0], edge + component[0] + longest[1]))
        return max(possible_bridges)

# print(strongest_longest_bridge(clean_puzzle(test), 0))
print(strongest_longest_bridge(clean_puzzle(puzzle), 0))