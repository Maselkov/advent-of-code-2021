from puzzleinput import lines

PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
PAIRS_R = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORE_TABLE = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_corrupted(line):
    stack = []
    for c in line:
        if c in PAIRS:
            stack.append(c)
        elif c in PAIRS.values():
            if stack.pop() != PAIRS_R[c]:
                return SCORE_TABLE[c]
    return 0


score = 0
for line in lines:
    score += find_corrupted(line)
print(score)
