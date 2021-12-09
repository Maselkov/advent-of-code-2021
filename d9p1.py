from puzzleinput import lines

grid = []
for line in lines:
    row = [int(x) for x in line]
    grid.append(row)
print(grid)


def check_adjacent(x, y):
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


total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if check_adjacent(x, y):
            risk_level = 1 + grid[y][x]
            print(x, y)
            print(risk_level)
            total += risk_level
print(total)
