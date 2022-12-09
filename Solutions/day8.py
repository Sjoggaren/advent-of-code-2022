from aocd.models import Puzzle


def solve(d):
    # print("input:, ", repr(d))

    grid = [[int(num) for num in l] for l in d.split("\n")]

    n = len(grid)
    m = len(grid[0])
    v = 0
    total = []

    for x in range(len(grid)):
        for y in range(len(grid)):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neigx = x + dx
                neigy = y + dy
                visible = True
                while neigx in range(n) and neigy in range(m):
                    if grid[neigx][neigy] >= grid[x][y]:
                        visible = False
                        break
                    neigx += dx
                    neigy += dy
                if visible:
                    v += 1

    s1 = v

    for x in range(len(grid)):
        for y in range(len(grid)):
            tree_score = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neigx = x + dx
                neigy = y + dy
                score = 0
                while neigx in range(n) and neigy in range(m):
                    if grid[neigx][neigy] >= grid[x][y]:
                        visible = False
                        break
                    neigx += dx
                    neigy += dy
                    score += 1
                tree_score.append(
                    score + (1 if neigx in range(n) and neigy in range(m) else 0)
                )
            total.append(tree_score[0] * tree_score[1] * tree_score[2] * tree_score[3])

    s2 = max(total)

    return s1, s2


puzzle = Puzzle(2022, 8)

input = puzzle.input_data
s1, s2 = solve(input)

print("Part 1 solution: ", s1)
print("Part 2 solution: ", s2)


# puzzle.answer_a = 3
# puzzle.answer_b = 4
