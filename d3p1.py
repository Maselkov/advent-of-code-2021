from puzzleinput import lines

numbers = []
for line in lines:
    numbers.append(int(line, 2))
gamma = 0
epsilon = 0
for i in reversed(list(range(len(lines[0])))):
    print(i)
    set_bits = 0
    unset_bits = 0
    for number in numbers:
        if number & (1 << i):
            set_bits += 1
        else:
            unset_bits += 1
    bit = 0
    if set_bits > unset_bits:
        bit = 1
    gamma |= bit << i
    epsilon |= int(not bool(bit)) << i
print(gamma * epsilon)
