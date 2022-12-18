import collections as coll
import re
import functools

# from utils import *
# from grid import Grid
from aocd.models import Puzzle


def bfs(start, dict):
    flows = []
    vistited = set()
    queue = coll.deque()

    queue.append((start, 0))
    vistited.add(start)

    while queue:
        s, dist = queue.popleft()

        for neighbour in dict[s][1]:
            if neighbour in vistited:
                continue
            queue.append((neighbour, dist + 1))
            vistited.add(neighbour)
            if dict[neighbour][0] > 0:
                flows.append((dist + 1, neighbour, dict[neighbour][0]))

    return flows


def highest_pressure(start, start_steps, possible_moves):
    @functools.cache
    def inner(pos, steps, opened):

        max_pressure = 0

        for dist, neighbour, flow in possible_moves[pos]:
            if steps - dist - 1 <= 0 or neighbour in opened:
                continue
            pressure = inner(
                neighbour, steps - dist - 1, opened | {neighbour}
            ) + flow * (steps - dist - 1)
            max_pressure = max(max_pressure, pressure)

        return max_pressure

    return inner(start, start_steps, frozenset(start))


def solvep1(d):
    row = [x for x in d.split("\n")]
    valves = coll.defaultdict()

    for r in row:
        flow_rate = [int(j) for j in re.findall("(\d+)", r)]
        current_tunnel = [ct[-2:] for ct in re.findall("Valve ?[A-Z]+", r)]
        leads_to = re.split("valve?.\s", r)
        for i, flow in enumerate(flow_rate):
            valves[current_tunnel[i]] = (
                flow,
                [path.strip() for path in leads_to[1].split(",")],
            )

    possible_moves = {point: bfs(point, valves) for point in valves.keys()}

    return highest_pressure("AA", 30, possible_moves)


def solvep2(d):
    print("input:, ", repr(d))
    t = 0

    # inp = []
    # out = []

    # r = [x for x in d.split("\n")]
    # e = [[x for x in l.split("\n")] for l in d.split("\n")]

    return t


puzzle = Puzzle(2022, 16)
input = puzzle.input_data

with open("test.txt", "r") as f:
    solvep1(f.read())

print("Answer problem 1:", solvep1(input))
# print("Answer problem 2", solvep2(input))
