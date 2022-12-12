import collections as coll
from aocd.models import Puzzle


def index2d(list2d, value):
    return next(
        (i, j) for i, lst in enumerate(list2d) for j, x in enumerate(lst) if x == value
    )


def solvep1(d):
    maze = [[ord(x) for x in l] for l in d.split("\n")]
    start = index2d(maze, ord("S"))
    end = index2d(maze, ord("E"))

    queue = coll.deque()
    path = {}

    queue.append(start)
    sx, sy = start
    maze[sx][sy] = ord("a")

    path[start] = 0
    ex, ey = end
    maze[ex][ey] = ord("z")

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
            if (
                0 <= nx < len(maze)
                and 0 <= ny < len(maze[0])
                and (nx, ny) not in path
                and (maze[nx][ny] - maze[x][y]) <= 1
            ):

                queue.append((nx, ny))
                path[(nx, ny)] = path[(x, y)] + 1

    return path[(ex, ey)]


def solvep2(d):

    maze = [[ord(x) for x in l] for l in d.split("\n")]
    start = index2d(maze, ord("S"))
    end = index2d(maze, ord("E"))

    queue = coll.deque()
    path = {}

    sx, sy = start
    maze[sx][sy] = ord("a")

    for x, row in enumerate(maze):
        for y, char in enumerate(row):
            if char == ord("a"):
                queue.append((x, y))
                path[(x, y)] = 0
    ex, ey = end
    maze[ex][ey] = ord("z")

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
            if (
                0 <= nx < len(maze)
                and 0 <= ny < len(maze[0])
                and (nx, ny) not in path
                and (maze[nx][ny] - maze[x][y]) <= 1
            ):

                queue.append((nx, ny))
                path[(nx, ny)] = path[(x, y)] + 1

    return path[(ex, ey)]


puzzle = Puzzle(2022, 12)
input = puzzle.input_data

print("Answer problem 1:", solvep1(input))
print("Answer problem 2", solvep2(input))
