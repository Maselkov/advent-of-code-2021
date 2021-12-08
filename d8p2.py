from puzzleinput import lines

notes = []
for line in lines:
    signals, output = line.split(" | ")
    signals = [set(s) for s in signals.split()]
    output = [list(s) for s in output.split()]
    notes.append((signals, output))

SEGMENTS = {
    tuple([0, 1, 2, 4, 5, 6]): 0,
    tuple([2, 5]): 1,
    tuple([0, 2, 3, 4, 6]): 2,
    tuple([0, 2, 3, 5, 6]): 3,
    tuple([1, 2, 3, 5]): 4,
    tuple([0, 1, 3, 5, 6]): 5,
    tuple([0, 1, 3, 4, 5, 6]): 6,
    tuple([0, 2, 5]): 7,
    tuple([0, 1, 2, 3, 4, 5, 6]): 8,
    tuple([0, 1, 2, 3, 5, 6]): 9
}

total = 0


def decode(layout, code):
    segments = tuple(sorted([layout[c] for c in code]))
    number = SEGMENTS[segments]
    return number


total = 0
for signals, output in notes:
    layout = [[], [], [], [], [], [], []]
    for signal in signals:
        if len(signal) == 2:
            layout[2].append(signal)
            layout[5].append(signal)
        if len(signal) == 3:
            layout[0].append(signal)
            layout[2].append(signal)
            layout[5].append(signal)
        if len(signal) == 4:
            layout[1].append(signal)
            layout[2].append(signal)
            layout[3].append(signal)
            layout[5].append(signal)
        if len(signal) == 7:
            layout[0].append(signal)
            layout[1].append(signal)
            layout[2].append(signal)
            layout[3].append(signal)
            layout[4].append(signal)
            layout[5].append(signal)
            layout[6].append(signal)
    new_layout = []
    for position in layout:
        possible_values = set.intersection(*position)
        new_layout.append(possible_values)
    layout = new_layout
    for values in layout:
        if len(values) == 2:
            one = values
        if len(values) == 3:
            seven = values
    a = seven - one
    new_layout = []
    for values in layout:
        if len(values) == 3:
            values = set(a)
        else:
            values.discard(a)
        new_layout.append(values)
    layout = new_layout

    for i in range(2):
        for position in layout:
            if len(position) == 1:
                letter = next(iter(position))
                for i in range(len(layout)):
                    if layout[i] != position:
                        layout[i].discard(letter)

    for signal in signals:
        if len(signal) == 6:
            possible_values = layout[2]
            for value in possible_values:
                if value not in signal:
                    c = value
            # possible_values = layout[3]
            # for value in possible_values:
            #     if value not in signal:
            #         d = value
    for i in range(len(layout)):
        if i == 2:
            layout[i] = set(c)
        else:
            layout[i].discard(c)
    for i in range(2):
        for position in layout:
            if len(position) == 1:
                letter = next(iter(position))
                for i in range(len(layout)):
                    if layout[i] != position:
                        layout[i].discard(letter)
    for signal in signals:
        if len(signal) == 6:
            possible_values = layout[3]
            for value in possible_values:
                if value not in signal:
                    d = value
    for i in range(len(layout)):
        if i == 3:
            layout[i] = set(d)
        else:
            layout[i].discard(d)
    for i in range(2):
        for position in layout:
            if len(position) == 1:
                letter = next(iter(position))
                for i in range(len(layout)):
                    if layout[i] != position:
                        layout[i].discard(letter)

    for signal in signals:
        if len(signal) == 6:
            possible_values = layout[4]
            for value in possible_values:
                if value not in signal:
                    e = value
    for i in range(len(layout)):
        if i == 4:
            layout[i] = set(e)
        else:
            layout[i].discard(e)
    segment_mapping = {}
    for i in range(len(layout)):
        segment_mapping[next(iter(layout[i]))] = i

    final_output = ""
    for signal in output:
        final_output += str(decode(segment_mapping, signal))
    print(final_output)
    total += int(final_output)
print(total)
