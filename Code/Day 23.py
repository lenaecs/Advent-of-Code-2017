import os.path
import math
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 23 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    line = line.strip()
    puzzle.append(line.split())

def is_prime(n):
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def coprocessor(inst):
    reg_dict = dict()
    for line in inst:
        try:
            int(line[1])
            pass
        except:
            reg_dict[line[1]] = 0
    i = 0
    mul = 0
    def resolve(instruction):
        try:
            int(instruction)
            return int(instruction)
        except:
            return reg_dict[instruction]
    while i < len(inst):
        if inst[i][0] == 'set':
            reg_dict[inst[i][1]] = resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'sub':
            reg_dict[inst[i][1]] -= resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'mul':
            reg_dict[inst[i][1]] *= resolve(inst[i][2])
            i += 1
            mul += 1
        elif inst[i][0] == 'jnz':
            if resolve(inst[i][1]) != 0:
                i += resolve(inst[i][2])
            else:
                i += 1
    return mul

# print(coprocessor(puzzle))

def a_to_1(inst):
    reg_dict = dict()
    for line in inst:
        try:
            int(line[1])
            pass
        except:
            reg_dict[line[1]] = 0
    i = 0
    reg_dict['a'] = 1
    def resolve(instruction):
        try:
            int(instruction)
            return int(instruction)
        except:
            return reg_dict[instruction]
    itts = 0
    i_list = []
    print(reg_dict)
    dict_list = []
    while i < len(inst) and itts < 100:
        # dict_list.append((i, reg_dict.copy(), inst[i]))
        # i_list.append(i)
        if inst[i][0] == 'set':
            reg_dict[inst[i][1]] = resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'sub':
            reg_dict[inst[i][1]] -= resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'mul':
            reg_dict[inst[i][1]] *= resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'jnz':
            if resolve(inst[i][1]) != 0:
                i += resolve(inst[i][2])
            else:
                i += 1
    #     itts += 1
    # for i in dict_list:
    #     if i[0] == 19:
    #         print(i)
    return reg_dict['h']

# print(a_to_1(puzzle))

def post_loop1(inst):
    reg_dict = dict()
    for line in inst:
        try:
            int(line[1])
            pass
        except:
            reg_dict[line[1]] = 0
    i = 0
    reg_dict['a'] = 1
    def resolve(instruction):
        try:
            int(instruction)
            return int(instruction)
        except:
            return reg_dict[instruction]
    itts = 0
    i_list = []
    dict_list = []
    while i < len(inst) and itts < 1000:
        dict_list.append((i, reg_dict.copy(), inst[i]))
        i_list.append(i)
        if i == 19:
            reg_dict['e'] = reg_dict['e'] - reg_dict['g']
            if not is_prime(reg_dict['b']):
                reg_dict['f'] = 0
            reg_dict['g'] = 0
            i += 1
        elif inst[i][0] == 'set':
            reg_dict[inst[i][1]] = resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'sub':
            reg_dict[inst[i][1]] -= resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'mul':
            reg_dict[inst[i][1]] *= resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'jnz':
            if resolve(inst[i][1]) != 0:
                i += resolve(inst[i][2])
            else:
                i += 1
        itts += 1
    for i in dict_list:
        print(i)
    return reg_dict['h']

# print(post_loop1(puzzle))
# not 4

h = 0
for x in range(108400, 125400 + 1, 17):
    for i in range(2, x):
        if x % i == 0:
            h += 1
            break
print(h)

# def post_loop2(inst):
#     reg_dict = {'h': 0, 'c': 125400, 'e': (125 +108274), 'f': 1, 'b' : 108400, 'a' : 1, 'g' : 1, 'd': 2}
#     i = 19
#     def resolve(instruction):
#         try:
#             int(instruction)
#             return int(instruction)
#         except:
#             return reg_dict[instruction]
#     itts = 0
#     i_list = []
#     dict_list = []
#     while i < len(inst) and itts < 1000:
#         dict_list.append((i, reg_dict.copy(), inst[i]))
#         i_list.append(i)
#         # add 1 to e, set g equal to e, g = g - b if d * e - b == 0 then set f to 0
#         if i == 19:
#             reg_dict['e']
#         elif inst[i][0] == 'set':
#             reg_dict[inst[i][1]] = resolve(inst[i][2])
#             i += 1
#         elif inst[i][0] == 'sub':
#             reg_dict[inst[i][1]] -= resolve(inst[i][2])
#             i += 1
#         elif inst[i][0] == 'mul':
#             reg_dict[inst[i][1]] *= resolve(inst[i][2])
#             i += 1
#         elif inst[i][0] == 'jnz':
#             if resolve(inst[i][1]) != 0:
#                 i += resolve(inst[i][2])
#             else:
#                 i += 1
#         itts += 1
#     for i in dict_list:
#         if i[0] == 19:
#             print(i)
#     return reg_dict['h']
#
# print(post_loop2(puzzle))