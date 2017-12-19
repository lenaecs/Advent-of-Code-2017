import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 9 Input.txt')
advent = open(path)

for line in advent:
    puzzle = line.strip()

test1 = '{}'
test2 = '{{{}}}'
test3 = '{{},{}}'
test4 = '{{{},{},{{}}}}'
test5 = '{<a>,<a>,<a>,<a>}'
test6 = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
test7 = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
test8 = '{{<a!>},{<a!>},{<a!>},{<ab>}}'

def group_count(stream):
    score = 0
    open_groups = 0
    garbage = False
    escape = False
    for i in stream:
        if escape == True:
            escape = False
        elif i == '!':
            escape = True
        elif garbage == True:
            if i == '>':
                garbage = False
        elif i == '<':
            garbage = True
        elif i == '{':
            open_groups += 1
            score += open_groups
        elif i == '}':
            open_groups -= 1
    return score

# print(group_count(test1))
# print(group_count(test2))
# print(group_count(test3))
# print(group_count(test4))
# print(group_count(test5))
# print(group_count(test6))
# print(group_count(test7))
# print(group_count(test8))

# print(group_count(puzzle))

test9 = '<>'
testa = '<random characters>'
testb = '<<<<>'
testc = '<{!>}>'
testd = '<!!>'
teste = '<!!!>>'
testf = '<{o"i!a,<{i<a>'

def trash_count(stream):
    score = 0
    open_groups = 0
    garbage = False
    escape = False
    trash = 0
    for i in stream:
        if escape == True:
            escape = False
        elif i == '!':
            escape = True
        elif garbage == True:
            if i == '>':
                garbage = False
            else:
                trash += 1
        elif i == '<':
            garbage = True
        elif i == '{':
            open_groups += 1
            score += open_groups
        elif i == '}':
            open_groups -= 1
    return trash

# print(trash_count(test9))
# print(trash_count(testa))
# print(trash_count(testb))
# print(trash_count(testc))
# print(trash_count(testd))
# print(trash_count(teste))
# print(trash_count(testf))

print(trash_count(puzzle))