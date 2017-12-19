import copy

def manhattan_distance(square):
    spot = 1
    side = 'right'
    grid = [[1]]
    while spot < square:
        if side == 'right':
            for i in range(len(grid) - 1, -1, -1):
                spot += 1
                grid[i].append(spot)
            side = 'top'
        elif side == 'top':
            top = []
            for i in range(len(grid[0])):
                spot += 1
                top = [spot] + top
            grid = [top] + grid
            side = 'left'
        elif side == 'left':
            for i in range(len(grid)):
                spot += 1
                grid[i] = [spot] + grid[i]
            side = 'bottom'
        elif side == 'bottom':
            bottom = []
            for i in range(len(grid[1])):
                spot += 1
                bottom.append(spot)
            grid.append(bottom)
            side = 'right'
    for i in range(len(grid)):
        if 1 in grid[i]:
            loc1 = (i, grid[i].index(1))
        if square in grid[i]:
            loc_square = (i, grid[i].index(square))
    dist = abs(loc1[0] - loc_square[0]) + abs(loc1[1] - loc_square[1])
    return dist

print(manhattan_distance(1))
print(manhattan_distance(12))
print(manhattan_distance(23))
print(manhattan_distance(1024))
print(manhattan_distance(347991))

def get_adjacent_cells(row, col, grid):
    adj_sum = 0
    grid_copy = copy.deepcopy(grid)
    grid_copy.append([0] * len(grid_copy[0]))
    grid_copy = [[0] * len(grid_copy[0])] + grid_copy
    for i in range(len(grid_copy)):
        to_replace = [0] + grid_copy[i] + [0]
        grid_copy[i] = to_replace
    row += 1
    col += 1
    adj_sum += grid_copy[row + 1][col]
    adj_sum += grid_copy[row + 1][col + 1]
    adj_sum += grid_copy[row][col + 1]
    adj_sum += grid_copy[row - 1][col + 1]
    adj_sum += grid_copy[row - 1][col]
    adj_sum += grid_copy[row - 1][col - 1]
    adj_sum += grid_copy[row][col - 1]
    adj_sum += grid_copy[row + 1][col - 1]
    return adj_sum

print(get_adjacent_cells(0, 1, [[1, 0]]))

def spiral_storage(square):
    side = 'right'
    grid = [[1]]
    spot = 1
    while spot < square:
        if side == 'right':
            for row in grid:
                row.append(0)
            for i in range(len(grid) - 1, -1, -1):
                grid_val = get_adjacent_cells(i, len(grid[i]) - 1, grid)
                if grid_val > square:
                    return grid_val
                grid[i][-1] = grid_val
            side = 'top'
        if side == 'top':
            grid = [[0] * len(grid[0])] + grid
            for i in range(len(grid[0]) - 1, -1, -1):
                grid_val = get_adjacent_cells(0, i, grid)
                if grid_val > square:
                    return grid_val
                grid[0][i] = grid_val
            side = 'left'
        if side == 'left':
            for i in range(len(grid)):
                to_replace = [0] + grid[i]
                grid[i] = to_replace
            for i in range(len(grid)):
                grid_val = get_adjacent_cells(i, 0, grid)
                if grid_val > square:
                    return grid_val
                grid[i][0] = grid_val
            side = 'bottom'
        if side == 'bottom':
            grid.append([0] * len(grid[0]))
            for i in range(len(grid[0])):
                grid_val = get_adjacent_cells(len(grid) - 1, i, grid)
                if grid_val > square:
                    return grid_val
                grid[-1][i] = grid_val
            side = 'right'



print(spiral_storage(347991))