from puzzleinput import numbers

increases = 0
window = float('inf')
for i in range(0, len(numbers) - 2):
    if sum(numbers[i:i + 3]) > window:
        increases += 1
    window = sum(numbers[i:i + 3])
print(increases)
