import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 16 Input.txt')
advent = open(path)

for line in advent:
    temp = line.strip()
    puzzle = temp.split(',')

test = ['s1', 'x3/4', 'pe/b']

def dance(group, steps):
    group_ls = list(group)
    for step in steps:
        if step[0] == 's':
            swaps = int(step[1:])
            group_ls = group_ls[-swaps:] + group_ls[:-swaps]
        if step[0] == 'x':
            swaps = step[1:].split('/')
            swaps[0], swaps[1] = int(swaps[0]), int(swaps[1])
            group_ls[swaps[0]], group_ls[swaps[1]] = group_ls[swaps[1]], group_ls[swaps[0]]
        if step[0] == 'p':
            swaps = step[1:].split('/')
            swaps[0] = group_ls.index(swaps[0])
            swaps[1] = group_ls.index(swaps[1])
            group_ls[swaps[0]], group_ls[swaps[1]] = group_ls[swaps[1]], group_ls[swaps[0]]
    return ''.join(group_ls)

# print(dance('abcde', test))
# print(dance('abcdefghijklmnop', puzzle))

def multiple_dances(group, steps, times):
    og = group
    reps = 0
    return_to_og = False
    group_sequence = []
    while return_to_og == False:
        reps += 1
        group = dance(group, steps)
        group_sequence.append(group)
        if group == og:
            return_to_og = True
    return group_sequence[(times % len(group_sequence)) - 1]

def stress_test(group, steps, times):
    for i in range(times):
        group = dance(group, steps)
    return group

# print(multiple_dances('abcde', test, 386))
# print(stress_test('abcde', test, 386))

print(multiple_dances('abcdefghijklmnop', puzzle, 1000000000))

# Not adpecliofbkgmjhn