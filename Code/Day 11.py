import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 11 Input.txt')
advent = open(path)

for line in advent:
    temp = line.strip()
    puzzle = temp.split(',')


test1 = ['ne', 'ne', 'ne']
test2 = ['ne', 'ne', 'sw', 'sw']
test3 = ['ne', 'ne', 's', 's']
test4 = ['se', 'sw', 'se', 'sw', 'sw']

def hex_grid(directions):
    x = 0
    y = 0
    z = 0
    for i in directions:
        if i == 'n':
            y += 1
            z -= 1
        elif i == 'ne':
            x += 1
            z -= 1
        elif i == 'se':
            x += 1
            y -= 1
        elif i == 's':
            y -= 1
            z += 1
        elif i == 'sw':
            x -= 1
            z += 1
        elif i == 'nw':
            x -= 1
            y += 1
    dist = (abs(x) + abs(y) + abs(z)) / 2
    return dist

print(hex_grid(test1))
print(hex_grid(test2))
print(hex_grid(test3))
print(hex_grid(test4))
print(hex_grid(puzzle))

# 581 is too low
# 676 is too high

def max_dist(directions):
    x = 0
    y = 0
    z = 0
    max_dist = 0
    for i in directions:
        if i == 'n':
            y += 1
            z -= 1
        elif i == 'ne':
            x += 1
            z -= 1
        elif i == 'se':
            x += 1
            y -= 1
        elif i == 's':
            y -= 1
            z += 1
        elif i == 'sw':
            x -= 1
            z += 1
        elif i == 'nw':
            x -= 1
            y += 1
        if (abs(x) + abs(y) + abs(z)) / 2 > max_dist:
            max_dist = (abs(x) + abs(y) + abs(z)) / 2
    return max_dist

print(max_dist(puzzle))