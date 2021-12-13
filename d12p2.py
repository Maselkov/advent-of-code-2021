from puzzleinput import lines
from collections import defaultdict
import copy

connections = []
for line in lines:
    a, b = line.split('-')
    connections.append((a, b))

points = defaultdict(set)
for a, b in connections:
    points[a].add(b)
    points[b].add(a)
small_caves = set(p for p in points
                  if p.islower() and p != "end" and p != "start")


def traverse(point, visited, visited_cave_twice):
    if point == "end":
        return 1
    if point in visited and point == "start":
        return 0
    if point in small_caves and point in visited:
        if not visited_cave_twice:
            visited_cave_twice = True
        else:
            return 0
    visited.add(point)
    paths = points[point]
    return sum(
        traverse(p, copy.copy(visited), visited_cave_twice) for p in paths)


print(traverse("start", set(), False))
