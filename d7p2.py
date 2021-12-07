from puzzleinput import lines
from functools import cache


@cache
def fuel_cost(diff):
    total = 0
    for i in range(1, diff + 1):
        total += i
    return total


crabs = [int(x) for x in lines[0].split(",")]
max_x = max(crabs)
lowest_cost_x = 0
lowest_fuel_cost = float('inf')
for x in range(max_x):
    total = 0
    for crab in crabs:
        total += fuel_cost(abs(crab - x))
    if total < lowest_fuel_cost:
        lowest_cost_x = x
        lowest_fuel_cost = total
print(lowest_fuel_cost)
