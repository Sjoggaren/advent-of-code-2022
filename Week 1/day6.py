from aocd.models import Puzzle


def solve(d):
    # print("input:, ", repr(d))
    solution = []

    for i in range(len(d)):
        uniq_chars = set(d[i : i + 4])
        if len(uniq_chars) == 4:
            solution.append(i + 4)
            break

    # Part 2
    for i in range(len(d)):
        uniq_chars = set(d[i : i + 14])
        if len(uniq_chars) == 14:
            solution.append(i + 14)
            break

    return solution


puzzle = Puzzle(2022, 6)

input = puzzle.input_data

solve(input)
puzzle.answer_a = solve(input)[0]
puzzle.answer_b = solve(input)[1]
