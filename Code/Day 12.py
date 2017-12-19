import queue
import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 12 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.strip())

test = ['0 <-> 2', '1 <-> 1', '2 <-> 0, 3, 4', '3 <-> 2, 4', '4 <-> 2, 3, 6', '5 <-> 6', '6 <-> 4, 5']

def list_cleanup(puzzle_list):
    puzzle_dict = dict()
    for line in puzzle_list:
        split_line = line.split()
        puzzle_dict[int(split_line[0])] = []
        for i in split_line[2:]:
            puzzle_dict[int(split_line[0])].append(int(i.strip(',')))
    return puzzle_dict

def reachable_programs(puzzle_list):
    puzzle_dict = list_cleanup(puzzle_list)
    bfs = queue.Queue()
    bfs.put(0)
    reachable = set([])
    reachable.add(0)
    while not bfs.empty():
        node = bfs.get()
        for i in puzzle_dict[node]:
            if i not in reachable:
                reachable.add(i)
                bfs.put(i)
    return len(reachable)

# print(reachable_programs(test))
# print(reachable_programs(puzzle))

def program_groups(puzzle_list):
    puzzle_dict = list_cleanup(puzzle_list)
    visited = set([])
    groups = 0
    for key in puzzle_dict:
        if key not in visited:
            groups += 1
            visited.add(key)
            bfs = queue.Queue()
            bfs.put(key)
            while not bfs.empty():
                node = bfs.get()
                for i in puzzle_dict[node]:
                    if i not in visited:
                        visited.add(i)
                        bfs.put(i)
    return groups

print(program_groups(test))
print(program_groups(puzzle))
