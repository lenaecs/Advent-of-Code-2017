advent = open('C:\\Users\LStoner\Desktop\Advent-Of-Code-2017\Input\Day 1 Input.txt')

for line in advent:
    puzzle = line.strip()

test1 = '1122'
test2 = '1111'
test3 = '1234'
test4 = '91212129'

def decaptia(str_input):
    key = 0
    for letter in range(len(str_input)):
        if str_input[letter - 1] == str_input[letter]:
            key += int(str_input[letter])
    return key

# print(decaptia(test1))
# print(decaptia(test2))
# print(decaptia(test3))
# print(decaptia(test4))
# print(decaptia(puzzle))

test1 = '1212'
test2 = '1221'
test3 = '123425'
test4 = '123123'
test5 = '12131415'

def decaptia2(str_input):
    key = 0
    for letter in range(len(str_input)):
        if str_input[int(letter - (len(str_input) / 2))] == str_input[letter]:
            key += int(str_input[letter])
    return key

print(decaptia2(test1))
print(decaptia2(test2))
print(decaptia2(test3))
print(decaptia2(test4))
print(decaptia2(test5))
print(decaptia2(puzzle))