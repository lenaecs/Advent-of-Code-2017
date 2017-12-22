import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 22 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.strip('\n'))

test = ['.........',
        '.........',
        '.........',
        '.....#...',
        '...#.....',
        '.........',
        '.........',
        '.........']

def map(dir):
    if dir == 0:
        return [-1, 0]
    elif dir == 1:
        return [0, 1]
    elif dir == 2:
        return [1, 0]
    elif dir == 3:
        return [0, -1]

def infector(puzzle, itts):
    cur_pos = [int(len(puzzle) / 2), int(len(puzzle[0])/ 2)]
    direction = 0
    infected = 0
    for string in range(len(puzzle)):
        puzzle[string] = list(puzzle[string])
    for i in range(itts):
        # for line in puzzle:
        #     print(line)
        if puzzle[cur_pos[0]][cur_pos[1]] == '#':
            direction = (direction + 1) % 4
            puzzle[cur_pos[0]][cur_pos[1]] = '.'
            cur_pos[0] += map(direction)[0]
            cur_pos[1] += map(direction)[1]
        elif puzzle[cur_pos[0]][cur_pos[1]] == '.':
            infected += 1
            direction = (direction - 1) % 4
            puzzle[cur_pos[0]][cur_pos[1]] = '#'
            cur_pos[0] += map(direction)[0]
            cur_pos[1] += map(direction)[1]
        if cur_pos[0] == -1:
            puzzle.insert(0, ['.'] * len(puzzle[0]))
            cur_pos[0] += 1
        elif cur_pos[0] == len(puzzle):
            puzzle.append(['.'] * len(puzzle[0]))
        if cur_pos[1] == -1:
            for line in puzzle:
                line.insert(0, '.')
            cur_pos[1] += 1
        elif cur_pos[1] == len(puzzle[0]):
            for line in puzzle:
                line.append('.')
        # print(direction, map(direction))
    return infected

# print(infector(test, 10000))
# print(infector(puzzle, 10000))

def immune_resistant(puzzle, itts):
    cur_pos = [int(len(puzzle) / 2), int(len(puzzle[0])/ 2)]
    direction = 0
    infected = 0
    for string in range(len(puzzle)):
        puzzle[string] = list(puzzle[string])
    for i in range(itts):
        # for line in puzzle:
        #     print(line)
        if puzzle[cur_pos[0]][cur_pos[1]] == '#':
            direction = (direction + 1) % 4
            puzzle[cur_pos[0]][cur_pos[1]] = 'F'
            cur_pos[0] += map(direction)[0]
            cur_pos[1] += map(direction)[1]
        elif puzzle[cur_pos[0]][cur_pos[1]] == '.':
            direction = (direction - 1) % 4
            puzzle[cur_pos[0]][cur_pos[1]] = 'W'
            cur_pos[0] += map(direction)[0]
            cur_pos[1] += map(direction)[1]
        elif puzzle[cur_pos[0]][cur_pos[1]] == 'W':
            infected += 1
            puzzle[cur_pos[0]][cur_pos[1]] = '#'
            cur_pos[0] += map(direction)[0]
            cur_pos[1] += map(direction)[1]
        elif puzzle[cur_pos[0]][cur_pos[1]] == 'F':
            direction = (direction + 2) % 4
            puzzle[cur_pos[0]][cur_pos[1]] = '.'
            cur_pos[0] += map(direction)[0]
            cur_pos[1] += map(direction)[1]
        if cur_pos[0] == -1:
            puzzle.insert(0, ['.'] * len(puzzle[0]))
            cur_pos[0] += 1
        elif cur_pos[0] == len(puzzle):
            puzzle.append(['.'] * len(puzzle[0]))
        if cur_pos[1] == -1:
            for line in puzzle:
                line.insert(0, '.')
            cur_pos[1] += 1
        elif cur_pos[1] == len(puzzle[0]):
            for line in puzzle:
                line.append('.')
        # print(direction, map(direction))
    return infected

# print(immune_resistant(test, 10000000))
print(immune_resistant(puzzle, 10000000))