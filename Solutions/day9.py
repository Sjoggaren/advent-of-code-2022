from aocd.models import Puzzle


moves = {"R": (1, 0), "U": (0, 1), "D": (0, -1), "L": (-1, 0)}


def solvep1(d):
    ins = [x for x in d.split("\n")]

    hx, hy = 0, 0
    tx, ty = 0, 0
    s1 = set()
    for i in ins:
        dx, dy = moves[i[0]]
        times = int(i[2:])
        for _ in range(times):
            hx += dx
            hy += dy
            while max(abs(tx - hx), abs(ty - hy)) > 1:
                if abs(tx - hx) > 0:
                    tx += 1 if hx > tx else -1
                if abs(ty - hy) > 0:
                    ty += 1 if hy > ty else -1
                s1.add((tx, ty))
    return len(s1)


def solvep2(d):

    ins = [x for x in d.split("\n")]

    rope = [(0, 0)] * 10
    s2 = set()

    for i in ins:
        dx, dy = moves[i[0]]
        times = int(i[2:])
        for _ in range(times):
            hx, hy = rope[0]
            rope[0] = hx + dx, hy + dy
            for j in range(1, len(rope)):
                # Compare previous x,y with current x,y
                px, py = rope[j - 1]
                cx, cy = rope[j]
                while max(abs(cx - px), abs(cy - py)) > 1:
                    if abs(cx - px) > 0:
                        cx += 1 if px > cx else -1
                    if abs(cy - py) > 0:
                        cy += 1 if py > cy else -1
                rope[j] = cx, cy

            s2.add(rope[-1])

    return len(s2)


puzzle = Puzzle(2022, 9)

input = puzzle.input_data
print(solvep2(input))


# puzzle.answer_a = 3
# puzzle.answer_b = 4
