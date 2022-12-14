from aocd.models import Puzzle


def get_sand_endpoint(s, my, part2=False):
    c = (500, 0)
    while True:
        if (c[0], c[1] + 1) not in s:
            c = (c[0], c[1] + 1)
        elif (c[0] - 1, c[1] + 1) not in s:
            c = (c[0] - 1, c[1] + 1)
        elif (c[0] + 1, c[1] + 1) not in s:
            c = (c[0] + 1, c[1] + 1)
        else:
            return c

        if part2 and c[1] == my - 1:
            return c
        if not part2 and c[1] >= my:
            return None


def solvep1(d):
    cave = set()
    row = [x for x in d.split("\n")]

    for r in row:
        s1 = r.split("->")
        for i in range(0, len(s1) - 1):
            x1, y1 = map(int, s1[i].split(","))
            x2, y2 = map(int, s1[i+1].split(","))

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cave.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    cave.add((x, y1))

    sand = set()
    my = max(y[1] for y in cave)
    while True:
        p = get_sand_endpoint(cave.union(sand), my)
        if p is None:
            break
        else:
            sand.add(p)

    return len(sand)


def solvep2(d):
    cave = set()
    row = [x for x in d.split("\n")]

    for r in row:
        s1 = r.split("->")
        for i in range(0, len(s1) - 1):
            x1, y1 = map(int, s1[i].split(","))
            x2, y2 = map(int, s1[i+1].split(","))

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cave.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    cave.add((x, y1))

    sand = set()
    my = max(y[1] for y in cave) + 2
    while True:
        p = get_sand_endpoint(cave.union(sand), my, True)
        if p is None:
            break
        else:
            sand.add(p)

        if p == (500, 0):
            break

    return len(sand)


puzzle = Puzzle(2022, 14)
input = puzzle.input_data

print("Answer problem 1:", solvep1(input))
print("Answer problem 2", solvep2(input))
