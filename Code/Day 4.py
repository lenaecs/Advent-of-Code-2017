import os.path
from os.path import dirname, abspath

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 4 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.split())

test = [['aa', 'bb', 'cc', 'dd', 'ee'],
        ['aa', 'bb', 'cc', 'dd', 'aa'],
        ['aa', 'bb', 'cc', 'dd', 'aaa']]

def count_valid_passwords(psw_list):
    valid_pass = 0
    for row in psw_list:
        psw_set = set([])
        valid = True
        for i in row:
            if i in psw_set:
                valid = False
                break
            psw_set.add(i)
        if valid == True:
            valid_pass += 1
    return valid_pass

# print(count_valid_passwords(test))
print(count_valid_passwords(puzzle))

test2 = [['abcde', 'fghij'],
         ['abcde', 'xyz', 'ecdab'],
         ['a', 'ab', 'abc', 'abd', 'abf', 'abj'],
         ['iiii', 'oiii', 'ooii', 'oooi', 'oooo'],
         ['oiii', 'ioii', 'iioi', 'iiio']]

test3 = [['oiii', 'ioii', 'iioi', 'iiio']]

def count_valid_anagrams(psw_list):
    valid_pass = 0
    for row in psw_list:
        psw_set = set([])
        valid = True
        for i in row:
            sorted_word = ''.join(sorted(i))
            if sorted_word in psw_set:
                valid = False
                break
            psw_set.add(sorted_word)
        if valid == True:
            valid_pass += 1
    return valid_pass

# print(count_valid_anagrams(test2))
# print(count_valid_anagrams(test3))

print(count_valid_anagrams(puzzle))