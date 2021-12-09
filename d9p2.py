from puzzleinput import lines
import math

grid = []
for line in lines:
    row = [int(x) for x in line]
    grid.append(row)


def check_low_point(x, y):
    value = grid[y][x]
    low_point = True
    for i in range(-1, 2, 2):
        try:
            if y + i < 0:
                raise IndexError
            if grid[y + i][x] <= value:
                low_point = False
        except IndexError:
            pass
        try:
            if x + i < 0:
                raise IndexError
            if grid[y][x + i] <= value:
                low_point = False
        except IndexError:
            continue
    return low_point


BASIN_POINTS = []


def calculate_basin_size(x, y):
    value = grid[y][x]
    if value == 9:
        return 0
    if (x, y) in BASIN_POINTS:
        return 0
    BASIN_POINTS.append((x, y))
    total = 1
    for i in range(-1, 2, 2):
        try:
            if y + i < 0:
                raise IndexError
            if grid[y + i][x] > value:
                total += calculate_basin_size(x, y + i)
        except IndexError:
            pass
        try:
            if x + i < 0:
                raise IndexError
            if grid[y][x + i] > value:
                total += calculate_basin_size(x + i, y)
        except IndexError:
            continue
    return total


total = 0
basins = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if check_low_point(x, y):
            basin_size = calculate_basin_size(x, y)
            BASIN_POINTS = []
            basins.append(basin_size)

print(math.prod(sorted(basins, reverse=True)[:3]))
