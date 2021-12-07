from puzzleinput import lines
commands = []

horizontal = 0
depth = 0
aim = 0

for line in lines:
    command, value = line.split()
    value = int(value)
    match command:
        case "forward":
            horizontal += value
            depth += aim * value
        case "down":
            aim += value
        case "up":
            aim -= value

print(horizontal*depth)
