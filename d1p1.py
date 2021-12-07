from puzzleinput import numbers

increases = 0
previous = numbers[0]
for depth in numbers:
    if depth > previous:
        increases += 1
    previous = depth
print(increases)
