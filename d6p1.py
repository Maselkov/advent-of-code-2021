from puzzleinput import lines

fish = [int(x) for x in lines[0].split(',')]

for _ in range(80):
    next_day_fish = []
    for fis in fish:
        if fis == 0:
            next_day_fish.append(8)
            fis = 6
        else:
            fis -= 1
        next_day_fish.append(fis)
    fish = next_day_fish
print(len(fish))
