from aocd.models import Puzzle


def solve(d):
    print("input:, ", repr(d))

    signal = [x for x in d.split("\n")]

    values = [1]
    for line in signal:
        inst = line.split(" ")
        if inst[0] == "noop":
            values.append(values[-1])
        else:
            n = int(inst[1])
            values.append(values[-1])
            values.append(values[-1] + n)

    s1 = (sum([values[cycle - 1] * cycle for cycle in range(20, 221, 40)]))
    print(values)
    i = 0
    for h in range(6):
        for w in range(40):
            if w in [values[i] - 1, values[i], values[i] + 1]:
                print("#", end="")
            else:
                print(" ", end="")
            i += 1
        print("")

    return s1


puzzle = Puzzle(2022, 10)
input = puzzle.input_data
solve(input)


# puzzle.answer_a = 3
# puzzle.answer_b = 4
