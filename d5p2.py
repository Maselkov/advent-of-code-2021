from puzzleinput import lines as points
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
lines = []
maximum_x = 0
maximum_y = 0
for line in points:
    first, second = line.split(' -> ')
    first = Point(*[int(x) for x in first.split(',')])
    second = Point(*[int(x) for x in second.split(',')])
    if first.x > maximum_x:
        maximum_x = first.x
    if first.y > maximum_y:
        maximum_y = first.y
    if second.x > maximum_x:
        maximum_x = second.x
    if second.y > maximum_y:
        maximum_y = second.y
    line = (first, second)
    lines.append(line)
grid = [[0 for _ in range(maximum_x + 1)] for _ in range(maximum_y + 1)]
for line in lines:
    first, second = line
    if first.x == second.x:
        diff = first.y - second.y
        if diff < 0:
            rang = range(first.y, second.y + 1)
        else:
            rang = range(first.y, second.y - 1, -1)
        for i in rang:
            grid[i][first.x] += 1
    elif first.y == second.y:
        diff = first.x - second.x
        if diff < 0:
            rang = range(first.x, second.x + 1)
        else:
            rang = range(first.x, second.x - 1, -1)
        for i in rang:
            grid[first.y][i] += 1
    else:
        diff_y = first.y - second.y
        diff_x = first.x - second.x
        if diff_x > 0:
            x_increment = -1
        else:
            x_increment = 1
        if diff_y > 0:
            y_increment = -1
        else:
            y_increment = 1
        for i in range(abs(diff_x) + 1):
            grid[first.y + i * y_increment][first.x + i * x_increment] += 1
overlapping = 0
for row in grid:
    for point in row:
        if point >= 2:
            overlapping += 1
print(overlapping)
