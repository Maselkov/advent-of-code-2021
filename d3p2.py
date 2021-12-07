from puzzleinput import lines

numbers = []
for line in lines:
    numbers.append(int(line, 2))


def find_o2_rating(numbers, k):
    set_bits = 0
    unset_bits = 0
    set_numbers = []
    unset_numbers = []
    for number in numbers:
        if number & (1 << k):
            set_numbers.append(number)
            set_bits += 1
        else:
            unset_numbers.append(number)
            unset_bits += 1
    if set_bits > unset_bits:
        if len(set_numbers) == 1:
            return set_numbers[0]
        return find_o2_rating(set_numbers, k - 1)
    elif set_bits < unset_bits:
        if len(unset_numbers) == 1:
            return unset_numbers[0]
        return find_o2_rating(unset_numbers, k - 1)
    else:
        if len(set_numbers) == 1:
            return set_numbers[0]
        return find_o2_rating(set_numbers, k - 1)


def find_co2_rating(numbers, k):
    set_bits = 0
    unset_bits = 0
    set_numbers = []
    unset_numbers = []
    for number in numbers:
        if number & (1 << k):
            set_numbers.append(number)
            set_bits += 1
        else:
            unset_numbers.append(number)
            unset_bits += 1
    if set_bits > unset_bits:
        if len(unset_numbers) == 1:
            return unset_numbers[0]
        return find_co2_rating(unset_numbers, k - 1)
    elif unset_bits > set_bits:
        if len(set_numbers) == 1:
            return set_numbers[0]
        return find_co2_rating(set_numbers, k - 1)
    else:
        if len(unset_numbers) == 1:
            return unset_numbers[0]
        return find_co2_rating(unset_numbers, k - 1)


o2 = find_o2_rating(numbers, len(lines[0]) - 1)
co2 = find_co2_rating(numbers, len(lines[0]) - 1)
print(co2 * o2)
