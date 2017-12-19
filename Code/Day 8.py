import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 8 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.split())

test = ['b inc 5 if a > 1', 'a inc 1 if b < 5', 'c dec -10 if a >= 1', 'c inc -20 if c == 10']

test2 = []
for line in test:
    test2.append(line.split())

def register_vals(puzzle):
    registers = dict()
    for inst in puzzle:
        if inst[0] not in registers:
            registers[inst[0]] = 0
        if inst[4] not in registers:
            registers[inst[4]] = 0
        run_calc = False
        if inst[5] == '>':
            if registers[inst[4]] > int(inst[6]):
                run_calc = True
        elif inst[5] == '<':
            if registers[inst[4]] < int(inst[6]):
                run_calc = True
        elif inst[5] == '==':
            if registers[inst[4]] == int(inst[6]):
                run_calc = True
        elif inst[5] == '!=':
            if registers[inst[4]] != int(inst[6]):
                run_calc = True
        elif inst[5] == '>=':
            if registers[inst[4]] >= int(inst[6]):
                run_calc = True
        elif inst[5] == '<=':
            if registers[inst[4]] <= int(inst[6]):
                run_calc = True
        if run_calc == True:
            if inst[1] == 'inc':
                registers[inst[0]] += int(inst[2])
            elif inst[1] == 'dec':
                registers[inst[0]] -= int(inst[2])
    max_reg = float('-inf')
    for key in registers:
        if registers[key] > max_reg:
            max_reg = registers[key]
    return max_reg

# print(register_vals(test2))
# print(register_vals(puzzle))

def register_max_val(puzzle):
    registers = dict()
    max_reg = float('-inf')
    for inst in puzzle:
        if inst[0] not in registers:
            registers[inst[0]] = 0
        if inst[4] not in registers:
            registers[inst[4]] = 0
        run_calc = False
        if inst[5] == '>':
            if registers[inst[4]] > int(inst[6]):
                run_calc = True
        elif inst[5] == '<':
            if registers[inst[4]] < int(inst[6]):
                run_calc = True
        elif inst[5] == '==':
            if registers[inst[4]] == int(inst[6]):
                run_calc = True
        elif inst[5] == '!=':
            if registers[inst[4]] != int(inst[6]):
                run_calc = True
        elif inst[5] == '>=':
            if registers[inst[4]] >= int(inst[6]):
                run_calc = True
        elif inst[5] == '<=':
            if registers[inst[4]] <= int(inst[6]):
                run_calc = True
        if run_calc == True:
            if inst[1] == 'inc':
                registers[inst[0]] += int(inst[2])
            elif inst[1] == 'dec':
                registers[inst[0]] -= int(inst[2])
        if registers[inst[0]] > max_reg:
            max_reg = registers[inst[0]]
    return max_reg

print(register_max_val(puzzle))