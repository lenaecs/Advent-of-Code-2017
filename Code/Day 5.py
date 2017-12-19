import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 5 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(int(line.strip()))

test = [0, 3, 0, 1, -3]

def maze(puzzle):
    location = 0
    itt = 0
    while location < len(puzzle):
        itt += 1
        new_location = location + puzzle[location]
        puzzle[location] += 1
        location = new_location
    return itt

# print(maze(test))
# print(maze(puzzle))

def maze2(puzzle):
    location = 0
    itt = 0
    while location < len(puzzle):
        itt += 1
        new_location = location + puzzle[location]
        if puzzle[location] >= 3:
            puzzle[location] -= 1
        else:
            puzzle[location] += 1
        location = new_location
    return itt

print(maze2(test))
print(maze2(puzzle))