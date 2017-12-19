import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 18 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    line = line.strip()
    puzzle.append(line.split())

test = ['set a 1', 'add a 2', 'mul a a', 'mod a 5', 'snd a', 'set a 0', 'rcv a', 'jgz a -1', 'set a 1', 'jgz a -2']

for i in range(len(test)):
    test[i] = test[i].split()


def duet(inst):
    last_sound = 0
    reg_dict = dict()
    for line in inst:
        reg_dict[line[1]] = 0
    i = 0

    def resolve(instruction):
        try:
            int(instruction)
            return int(instruction)
        except:
            return reg_dict[instruction]
    print(reg_dict)
    while i < len(inst):
        if inst[i][0] == 'snd':
            last_sound = reg_dict[inst[i][1]]
            i += 1
        elif inst[i][0] == 'set':
            reg_dict[inst[i][1]] = resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'add':
            reg_dict[inst[i][1]] += resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'mul':
            reg_dict[inst[i][1]] *= resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'mod':
            reg_dict[inst[i][1]] %= resolve(inst[i][2])
            i += 1
        elif inst[i][0] == 'rcv':
            if reg_dict[inst[i][1]] != 0 and last_sound != 0:
                return last_sound
            i += 1
        elif inst[i][0] == 'jgz':
            if resolve(inst[i][1]) > 0:
                i += resolve(inst[i][2])
            else:
                i += 1

# print(duet(test))
# print(duet(puzzle))

class Program():
    def __init__(self, program_id, inst):
        self.reg_dict = {'a' : 0, 'b' : 0, 'i': 0, 'f' : 0, 'p' : program_id}
        self.i = 0
        self.inst = inst

    def resolve(self, instruction):
        try:
            int(instruction)
            return int(instruction)
        except:
            return self.reg_dict[instruction]

    def run_program(self, recieved_list):
        send_list = []
        while self.i < len(self.inst):
            if self.inst[self.i][0] == 'snd':
                send_list.append(self.resolve(self.inst[self.i][1]))
                self.i += 1
            elif self.inst[self.i][0] == 'set':
                self.reg_dict[self.inst[self.i][1]] = self.resolve(self.inst[self.i][2])
                self.i += 1
            elif self.inst[self.i][0] == 'add':
                self.reg_dict[self.inst[self.i][1]] += self.resolve(self.inst[self.i][2])
                self.i += 1
            elif self.inst[self.i][0] == 'mul':
                self.reg_dict[self.inst[self.i][1]] *= self.resolve(self.inst[self.i][2])
                self.i += 1
            elif self.inst[self.i][0] == 'mod':
                self.reg_dict[self.inst[self.i][1]] %= self.resolve(self.inst[self.i][2])
                self.i += 1
            elif self.inst[self.i][0] == 'jgz':
                if self.resolve(self.inst[self.i][1]) > 0:
                    self.i += self.resolve(self.inst[self.i][2])
                else:
                    self.i += 1
            elif self.inst[self.i][0] == 'rcv':
                if recieved_list == []:
                    break
                else:
                    self.reg_dict[self.inst[self.i][1]] = recieved_list.pop(0)
                    self.i += 1
        return send_list

temp = ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']
test2 = []
for val in temp:
    test2.append(val.split())

def tail_of_two_programs(puzzle):
    Program0 = Program(0, puzzle)
    Program1 = Program(1, puzzle)
    send_list0 = Program0.run_program([])
    send_list1 = Program1.run_program(send_list0)
    sent_count = len(send_list1)
    while send_list0 != [] or send_list1 != []:
        send_list0 = Program0.run_program(send_list1)
        send_list1 = Program1.run_program(send_list0)
        sent_count += len(send_list1)
    return sent_count

print(tail_of_two_programs(puzzle))

# Not 127