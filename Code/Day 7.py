import os.path
from os.path import dirname, abspath
import queue

path = os.path.join(dirname(dirname(abspath(__file__))), 'Input/Day 7 Input.txt')
advent = open(path)

puzzle = []
for line in advent:
    puzzle.append(line.split())

test = [['pbga', '(66)'],
        ['xhth', '(57)'],
        ['ebii', '(61)'],
        ['havc', '(66)'],
        ['ktlj', '(57)'],
        ['fwft', '(72)', '->', 'ktlj', 'cntj', 'xhth'],
        ['qoyq', '(66)'],
        ['padx', '(45)', '->', 'pbga', 'havc', 'qoyq'],
        ['tknk', '(41)', '->', 'ugml', 'padx', 'fwft'],
        ['jptl', '(61)'],
        ['ugml', '(68)', '->', 'gyxo', 'ebii', 'jptl'],
        ['gyxo', '(61)'],
        ['cntj', '(57)']]


def input_cleanup(tree_list):
    tree_dict = dict()
    for tree in tree_list:
        if len(tree) == 2:
            tree_dict[tree[0]] = [int(tree[1].strip('()')), []]
        else:
            leaf_list = []
            for leaf in tree[3:]:
                leaf_list.append(leaf.strip(','))
            tree_dict[tree[0]] = [int(tree[1].strip('()')), leaf_list]
    return tree_dict

def root_find(tree_list):
    tree_dict = input_cleanup(tree_list)
    root_first = dict()
    for key in tree_dict:
        root_first[key] = []
    for key in root_first:
        for node in tree_dict[key][1]:
            root_first[node].append(key)
    for key in root_first:
        if root_first[key] == []:
            return key, root_first

# print(root_find(test))
# print(root_find(puzzle))

def get_weight(node, tree_dict):
    if tree_dict[node][1] == []:
        return tree_dict[node][0]
    else:
        weight = tree_dict[node][0]
        for i in tree_dict[node][1]:
            weight += get_weight(i, tree_dict)
        return weight

def unbalance_find(tree_list):
    tree_dict = input_cleanup(tree_list)
    root, root_first = root_find(tree_list)
    root_queue = queue.Queue()
    root_queue.put(root)
    while not root_queue.empty():
        node = root_queue.get()
        tree_dict[node].append(get_weight(node, tree_dict))
        for i in tree_dict[node][1]:
            root_queue.put(i)
    root_queue.put(root)
    while not root_queue.empty():
        node = root_queue.get()
        first_node = tree_dict[node][1][0]
        weight_comp = tree_dict[first_node][2]
        for leaf in tree_dict[node][1]:
            if weight_comp != tree_dict[leaf][2]:
                other_weight = tree_dict[leaf][2]
        weight1_list = []
        weight2_list = []
        for leaf in tree_dict[node][1]:
            if tree_dict[leaf][2] == weight_comp:
                weight1_list.append(leaf)
            else:
                weight2_list.append(leaf)
        if len(weight1_list) == 1:
            weight_diff = other_weight - weight_comp
            possible_weight = tree_dict[weight1_list[0]][0] + weight_diff
            root_queue.put(weight1_list[0])
        elif len(weight2_list) == 1:
            weight_diff = weight_comp - other_weight
            possible_weight = tree_dict[weight2_list[0]][0] + weight_diff
            root_queue.put(weight2_list[0])
    return possible_weight


print(unbalance_find(test))
print(unbalance_find(puzzle))
# 45774 is too high