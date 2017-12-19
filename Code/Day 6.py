import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 6 Input.txt')
advent = open(path)

for line in advent:
    puzzle = [int(x) for x in line.split()]

print(puzzle)

test = [0, 2, 7, 0]

def memory_dist(banks):
    step = 0
    scene_states = set([])
    cur_state = banks
    state_string = ''
    for i in banks:
        state_string += str(i) + '-'
    while state_string not in scene_states:
        scene_states.add(state_string)
        max_mem = max(cur_state)
        max_index = cur_state.index(max_mem)
        new_state = list(cur_state)
        new_state[max_index] = 0
        for bank in range(len(new_state)):
            new_state[bank] += int(max_mem / len(new_state))
            if (bank - max_index) % len(new_state) <= max_mem % len(new_state) and bank != max_index:
                new_state[bank] += 1
        state_string = ''
        for i in new_state:
            state_string += str(i) + '-'
        cur_state = new_state
        step += 1
    return step

# print(memory_dist(test))
# print(memory_dist(puzzle))

def size_of_loop(banks):
    step = 0
    scene_states = set([])
    cur_state = banks
    state_string = ''
    for i in banks:
        state_string += str(i) + '-'
    while state_string not in scene_states:
        scene_states.add(state_string)
        max_mem = max(cur_state)
        max_index = cur_state.index(max_mem)
        new_state = list(cur_state)
        new_state[max_index] = 0
        for bank in range(len(new_state)):
            new_state[bank] += int(max_mem / len(new_state))
            if (bank - max_index) % len(new_state) <= max_mem % len(new_state) and bank != max_index:
                new_state[bank] += 1
        state_string = ''
        for i in new_state:
            state_string += str(i) + '-'
        cur_state = new_state
    goal_state = state_string
    state_string = ''
    while state_string != goal_state:
        max_mem = max(cur_state)
        max_index = cur_state.index(max_mem)
        new_state = list(cur_state)
        new_state[max_index] = 0
        for bank in range(len(new_state)):
            new_state[bank] += int(max_mem / len(new_state))
            if (bank - max_index) % len(new_state) <= max_mem % len(new_state) and bank != max_index:
                new_state[bank] += 1
        state_string = ''
        for i in new_state:
            state_string += str(i) + '-'
        cur_state = new_state
        step += 1
    return step

print(size_of_loop(test))
print(size_of_loop(puzzle))