import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 13 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.strip())

test = ['0: 3', '1: 2', '4: 4', '6: 4']

def input_cleanup(wall_list):
    wall_dict = dict()
    for i in wall_list:
        i_split = i.split(': ')
        wall_dict[int(i_split[0])] = int(i_split[1])
    return wall_dict

def trip_severity(wall_list):
    wall_dict = input_cleanup(wall_list)
    severity = 0
    for i in range(max(wall_dict) + 1):
        if i not in wall_dict:
            pass
        elif wall_dict[i] == 1:
            severity += i
        elif i % ((wall_dict[i] - 1) * 2) == 0:
            severity += i * wall_dict[i]
    return severity

# print(trip_severity(test))
print(trip_severity(puzzle))

def trip_delay(wall_list):
    wall_dict = input_cleanup(wall_list)
    caught = True
    delay = -1
    while caught == True:
        caught = False
        delay += 1
        for i in range(max(wall_dict) + 1):
            if i not in wall_dict:
                pass
            elif (i + delay) % ((wall_dict[i] - 1) * 2) == 0:
                caught = True
    return delay

print(trip_delay(test))
print(trip_delay(puzzle))