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

for fold in folds:
    coord_index = 0 if fold[0] == "x" else 1
    dots_to_fold = [d for d in dots if d[coord_index] > fold[1]]
    maximum = max(d[coord_index] for d in dots_to_fold)
    for dot in dots_to_fold:
        dots.remove(dot)
        dot = list(dot)
        dot[coord_index] = maximum - dot[coord_index]
        dots.add(tuple(dot))
    print(len(dots))
    exit()
