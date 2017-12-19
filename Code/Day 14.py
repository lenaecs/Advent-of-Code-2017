import queue

test = 'flqrgnkx'
puzzle = 'ljoxqyyw'

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def knot_hash(hash_len, dir_string):
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

def get_neighbors(row, col, height, width):
    xs = []
    ys = []
    if row == 0:
        xs.append(row + 1)
    elif row == height - 1:
        xs.append(row - 1)
    else:
        xs.append(row + 1)
        xs.append(row - 1)
    if col == 0:
        ys.append(col + 1)
    elif col == width - 1:
        ys.append(col - 1)
    else:
        ys.append(col + 1)
        ys.append(col - 1)
    results = []
    for x in xs:
        results.append((x, col))
    for y in ys:
        results.append((row, y))
    return results

def defragment(puzzle):
    squares = 0
    for i in range(128):
        knot = knot_hash(256, puzzle + '-' + str(i))
        for j in knot:
            if is_number(j):
                unclean_bin = bin(int(j))
            else:
                unclean_bin = bin(ord(j) - 87)
            unclean_bin = unclean_bin[2:]
            for digit in unclean_bin:
                squares += int(digit)
    return squares

# print(defragment(test))
# print(defragment(puzzle))

def regions(puzzle):
    grid = []
    for i in range(128):
        knot = knot_hash(256, puzzle + '-' + str(i))
        row = []
        for j in knot:
            if is_number(j):
                unclean_bin = bin(int(j))
            else:
                unclean_bin = bin(ord(j) - 87)
            unclean_bin = unclean_bin[2:]
            for digit in range(4 - len(unclean_bin)):
                row.append(0)
            for digit in unclean_bin:
                row.append(int(digit))
        grid.append(row)
    visited = []
    for i in range(len(grid)):
        visited.append([0] * len(grid[0]))
    groups = 0
    for row in range(len(visited)):
        for col in range(len(visited)):
            if grid[row][col] == 1 and visited[row][col] == 0:
                groups += 1
                visited[row][col] = 1
                bfs = queue.Queue()
                bfs.put((row, col))
                while not bfs.empty():
                    coord = bfs.get()
                    for neighbor in get_neighbors(coord[0], coord[1], len(grid), len(grid[0])):
                        if grid[neighbor[0]][neighbor[1]] == 1 and visited[neighbor[0]][neighbor[1]] == 0:
                            visited[neighbor[0]][neighbor[1]] = 1
                            bfs.put(neighbor)
    return groups


# print(regions(test))
print(regions(puzzle))