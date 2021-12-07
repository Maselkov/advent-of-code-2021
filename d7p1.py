from collections import Counter

from puzzleinput import lines

crabs = [int(x) for x in lines[0].split(",")]
max_x = max(crabs)
lowest_cost_x = 0
lowest_fuel_cost = float('inf')
for x in range(max_x):
    total = 0
    for crab in crabs:
        total += abs(crab - x)
    if total < lowest_fuel_cost:
        lowest_cost_x = x
        lowest_fuel_cost = total
print(lowest_fuel_cost)
