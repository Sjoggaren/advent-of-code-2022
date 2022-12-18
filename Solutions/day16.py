import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
import functools

# from utils import *
# from grid import Grid
from aocd.models import Puzzle

def bfs(start, dict):
    pass


def highest_pressure(start, steps, dict, memo, open):
    # No moves left return flowrate of current valve
    if steps == 0:
        return 0

    # Check if we already calculated this state
    if (start, steps, open) in memo:
        return memo[(start, steps, open)]

    max_pressure = 0

    # Take an action to turn valve
    if steps > 0 and start not in open:

        
        pressure = (
            highest_pressure(start, steps - 1, dict, memo, open | {start})
            + sum(dict[valve][0] for valve in open)
        )
        max_pressure = max(max_pressure, pressure)

    for j in dict[start][1]:
        # Take an action to go to another valve
        pressure = highest_pressure(j, steps - 1, dict, memo, open) + sum(dict[valve][0] for valve in open)
        max_pressure = max(max_pressure, pressure)

    memo[(start, steps, open)] = max_pressure

    return max_pressure


def solvep1(d):
    print("input:, ", repr(d))
    t = 0

    row = [x for x in d.split("\n")]
    print(row)
    # elem = [[x for x in l.split("\n")] for l in d.split("\n")]
    flow_rates = coll.defaultdict()
    
    for r in row:
        flow_rate = [int(j) for j in re.findall("(\d+)", r)]
        current_tunnel = [ct[-2:] for ct in re.findall("Valve ?[A-Z]+", r)]
        leads_to = re.split("valve?.\s", r)
        for i, flow in enumerate(flow_rate):
            flow_rates[current_tunnel[i]] = (
                flow,
                [path.strip() for path in leads_to[1].split(",")],
            )
    steps = 30
    memory = coll.defaultdict()
    open = frozenset()

    print(highest_pressure("AA", steps, flow_rates, memory, open))

    return t


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

#with open("test.txt", "r") as f:
#    solvep1(f.read())

print("Answer problem 1:", solvep1(input))
# print("Answer problem 2", solvep2(input))
