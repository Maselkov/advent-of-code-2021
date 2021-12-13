from puzzleinput import lines
from collections import defaultdict
import copy

connections = []
for line in lines:
    a, b = line.split('-')
    connections.append((a, b))

points = defaultdict(list)
for a, b in connections:
    points[a].append(b)
    points[b].append(a)
print(points)


def traverse(point, visited):
    if point == "end":
        return 1
    if point.islower() and point in visited:
        return 0
    visited.append(point)
    paths = points[point]
    return sum(traverse(p, copy.copy(visited)) for p in paths)


print(traverse("start", []))
