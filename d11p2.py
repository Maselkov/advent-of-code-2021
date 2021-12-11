from puzzleinput import lines

octopi = []
for line in lines:
    row = [int(x) for x in line]
    octopi.append(row)

FLASHED = []
octopus_count = len(octopi) * len(octopi[0])


def flash(x, y):
    FLASHED.append((x, y))
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if x == 0 and i == -1:
                continue
            if y == 0 and j == -1:
                continue
            if x == len(octopi) - 1 and i == 1:
                continue
            if y == len(octopi[0]) - 1 and j == 1:
                continue
            new_x = x + i
            new_y = y + j
            octopi[new_y][new_x] += 1
            if (new_x, new_y) not in FLASHED and octopi[new_y][new_x] > 9:
                flash(new_x, new_y)
    return 2


steps = 1000
for step in range(steps):
    FLASHED = []
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            octopi[y][x] += 1
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            if octopi[y][x] > 9:
                if (x, y) not in FLASHED:
                    flash(x, y)
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            if octopi[y][x] > 9:
                octopi[y][x] = 0
    if len(FLASHED) == octopus_count:
        print(step + 1)
        exit()
s
