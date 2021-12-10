from puzzleinput import lines
from statistics import median

PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
PAIRS_R = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORE_TABLE = {"(": 1, "[": 2, "{": 3, "<": 4}


def find_corrupted(line):
    stack = []
    for c in line:
        if c in PAIRS:
            stack.append(c)
        elif c in PAIRS.values():
            if stack.pop() != PAIRS_R[c]:
                return True
    return False


def autocomplete(line):
    stack = []
    for c in line:
        if c in PAIRS:
            stack.append(c)
        elif c in PAIRS.values():
            if stack.pop() != PAIRS_R[c]:
                return False
    score = 0
    for bracket in reversed(stack):
        score *= 5
        score += SCORE_TABLE[bracket]
    return score


incomplete = []
for line in lines:
    if not find_corrupted(line):
        incomplete.append(line)
scores = []
for line in incomplete:
    scores.append(autocomplete(line))
print(median(scores))
