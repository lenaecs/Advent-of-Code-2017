import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 2 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    numbers = [int(x) for x in line.split()]
    puzzle.append(numbers)

test = [[5, 1, 9, 5],
        [7, 5, 3,],
        [2, 4, 6, 8]]

def check_sum(grid):
    cur_sum = 0
    for row in grid:
        min_val = float('Inf')
        max_val = float('-Inf')
        for val in row:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
        cur_sum += max_val - min_val
    return cur_sum

print(check_sum(test))
print(check_sum(puzzle))

test2 = [[5, 9, 2, 8],
         [9, 4, 7, 3],
         [3, 8, 6, 5]]

def check_sum2(grid):
    cur_sum = 0
    for row in grid:
        for i in range(len(row)-1):
            for j in range(i + 1, len(row)):
                if row[i] % row[j] == 0:
                    cur_sum += int(row[i] / row[j])
                elif row[j] % row[i] == 0:
                    cur_sum += int(row[j] / row[i])
    return cur_sum

print(check_sum2(test2))
print(check_sum2(puzzle))