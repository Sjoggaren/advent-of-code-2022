from aocd.models import Puzzle


def solve(d):
    solution = []

    row = d.splitlines()
    # print(repr(row))

    init_stack, instructions = [[x for x in l.split("\n")] for l in d.split("\n\n")]
    # init_stack = [x.split(" ") for x in init_stack]
    # print(init_stack)
    stack = []
    for index, num in enumerate(init_stack[-1]):
        if num != " ":
            row_val = []
            for row in init_stack[:-1]:
                if row[index] != " ":
                    row_val.append(row[index])
            stack.append(row_val)

    s1 = stack

    for index, inst in enumerate(instructions):
        words = inst.split(" ")
        move = int(words[1])
        from_ = int(words[3])
        to = int(words[5])
        for i in range(move):
            val2 = s1[from_ - 1].pop(0)
            # Change '0' to 'i' for solution 1
            s1[to - 1].insert(i, val2)

    solution.append(s1)

    return solution


puzzle = Puzzle(2022, 5)
input = puzzle.input_data
solution = solve(input)
print("Solution : ", "".join(r[0] for r in solution[0]))

# puzzle.answer_a = 3
# puzzle.answer_b = 4
