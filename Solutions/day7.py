from aocd.models import Puzzle
from collections import defaultdict
import re


def solve(d):

    commands = [l for l in d.split("\n")]

    paths = []
    dirs = defaultdict(int)
    for instruction in commands:
        if "cd .." in instruction:
            paths.pop()
        elif re.match("\A[0-9]", instruction):
            for dir in paths:
                dirs[dir] += int(instruction[: instruction.index(" ")])
        elif "cd" in instruction:
            dir = instruction[instruction.index("cd") + 3 :]
            paths.append("".join(paths) + dir)

    s1 = sum(dirs[dir] if dirs[dir] <= 100000 else 0 for dir in dirs)

    unused_space = 30000000 - (70000000 - dirs["/"])

    s2 = min(dirs[dir] for dir in dirs if unused_space <= dirs[dir])

    return s1, s2


puzzle = Puzzle(2022, 7)
input = puzzle.input_data
s1, s2 = solve(input)

print("Part 1 solution: ", s1)
print("Part 2 solution: ", s2)
