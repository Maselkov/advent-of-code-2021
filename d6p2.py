from collections import Counter

from puzzleinput import lines

fish = Counter(int(x) for x in lines[0].split(","))
days = 256
for _ in range(days):
    next_fish = Counter()
    for i in range(9):
        if i == 0:
            next_fish[8] = fish[0]
            next_fish[6] = fish[0]
        else:
            next_fish[i - 1] += fish[i]
    fish = next_fish
print(sum(fish.values()))
