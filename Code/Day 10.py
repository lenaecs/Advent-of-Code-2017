import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 10 Input.txt')
advent = open(path)

for line in advent:
    char_puzzle = line.strip()
    temp = char_puzzle.split(',')
    puzzle = [int(x) for x in temp]

test = [3, 4, 1, 5]

def bad_hash(hash_len, dirs):
    number_cycle = list(range(hash_len))
    skip_size = 0
    pos = 0
    for i in dirs:
        list_to_rev = []
        for j in range(i):
            list_to_rev.append(number_cycle[(pos + j) % hash_len])
        list_to_rev.reverse()
        for j in range(i):
            number_cycle[(pos + j) % hash_len] = list_to_rev[j]
        pos += i + skip_size
        skip_size += 1
    return number_cycle[0] * number_cycle[1]

# print(bad_hash(5, test))
# print(bad_hash(256, puzzle))

test1 = ''
test2 = 'AoC 2017'
test3 = '1,2,3'
test4 = '1,2,4'

def more_hash(hash_len, dir_string):
    dirs = []
    for dir in dir_string:
        dirs.append(ord(dir))
    dirs += [17,31,73,47,23]
    number_cycle = list(range(hash_len))
    skip_size = 0
    pos = 0
    for h in range(64):
        for i in dirs:
            list_to_rev = []
            for j in range(i):
                list_to_rev.append(number_cycle[(pos + j) % hash_len])
            list_to_rev.reverse()
            for j in range(i):
                number_cycle[(pos + j) % hash_len] = list_to_rev[j]
            pos += i + skip_size
            skip_size += 1
    dense_hash = []
    for i in range(16):
        running_xor = number_cycle[i * 16]
        for j in range(1, 16):
            running_xor = running_xor ^ number_cycle[i * 16 + j]
        dense_hash.append(running_xor)
    fin_hash = ''
    for i in dense_hash:
        if len(hex(i)[2:]) == 1:
            fin_hash += '0' + hex(i)[2:]
        else:
            fin_hash += hex(i)[2:]
    return fin_hash

print(more_hash(256, test1))
print(more_hash(256, test2))
print(more_hash(256, test3))
print(more_hash(256, test4))
print(more_hash(256, char_puzzle))
