import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 19 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.strip('\n'))

test = ['     |          ',
        '     |  +--+    ',
        '     A  |  C    ',
        ' F---|----E|--+ ',
        '     |  |  |  D ',
        '     +B-+  +--+ ',
        '                ']

def maze(diagram):
    cur_loc = [0, diagram[0].index('|')]
    finish = False
    vel = [1, 0]
    guide_string = ''
    steps = 1
    while finish == False:
        cur_loc = [cur_loc[0] + vel[0], cur_loc[1] + vel[1]]
        steps += 1
        if diagram[cur_loc[0]][cur_loc[1]] in ['-', '|']:
            pass
        elif diagram[cur_loc[0]][cur_loc[1]] == '+':
            if diagram[cur_loc[0] + vel[0]][cur_loc[1] + vel[1]] == ' ':
                if abs(vel[0]) == 1:
                    if diagram[cur_loc[0]][cur_loc[1] + 1] != ' ':
                        vel = [0, 1]
                    elif diagram[cur_loc[0]][cur_loc[1] - 1] != ' ':
                        vel = [0, -1]
                elif abs(vel[1]) == 1:
                    if diagram[cur_loc[0] + 1][cur_loc[1]] != ' ':
                        vel = [1, 0]
                    elif diagram[cur_loc[0] - 1][cur_loc[1]] != ' ':
                        vel = [-1, 0]
        elif diagram[cur_loc[0]][cur_loc[1]].isalpha():
            guide_string += diagram[cur_loc[0]][cur_loc[1]]
            if diagram[cur_loc[0] + vel[0]][cur_loc[1] + vel[1]] == ' ':
                finish = True
    return guide_string, steps

print(maze(test))
print(maze(puzzle))