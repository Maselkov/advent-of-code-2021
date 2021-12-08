from puzzleinput import lines

notes = []
for line in lines:
    signals, output = line.split(" | ")
    signals = signals.split()
    output = output.split()
    notes.append((signals, output))

total = 0
for signals, output in notes:
    for value in output:
        if len(value) in (2, 4, 3, 7):
            total += 1
print(total)
