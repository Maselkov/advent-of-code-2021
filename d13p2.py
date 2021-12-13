from puzzleinput import lines

folds = []
dots = set()
for line in lines:
    if line.startswith("fold"):
        line = line.removeprefix("fold along ")
        coord, value = line.split("=")
        value = int(value)
        folds.append((coord, value))
    elif line.strip():
        x, y = (int(x) for x in line.split(","))
        dots.add((x, y))


def print_dots(dots, empty="░", full="█"):
    maximum_x = max(d[0] for d in dots)
    maximum_y = max(d[1] for d in dots)
    grid = [[empty for _ in range(maximum_x + 1)]
            for _ in range(maximum_y + 1)]
    for x, y in dots:
        grid[y][x] = full
    for row in grid:
        print("".join(row))


for fold in folds:
    coord_index = 0 if fold[0] == "x" else 1
    dots_to_fold = [d for d in dots if d[coord_index] > fold[1]]
    maximum = max(d[coord_index] for d in dots_to_fold)
    if maximum % 2:
        maximum += 1
    for dot in dots_to_fold:
        dots.remove(dot)
        dot = list(dot)
        dot[coord_index] = maximum - dot[coord_index]
        dots.add(tuple(dot))
print_dots(dots)
