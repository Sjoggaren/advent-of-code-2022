import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
#from utils import *
#from grid import Grid
from aocd.models import Puzzle

def solve(d):
    #print("input:, ", repr(d))
    t = 0
    
    row = [x for x in d.split("\n")]

    s1 = 0
    for entry in row:
        first = entry[slice(0,len(entry)//3)]
        second = entry[slice(len(entry)//3, len(entry))]
        f = coll.Counter(first)
        s = coll.Counter(second)
        keys = [k for k,v in f.items() for k2,v2 in s.items() if k==k2]
        s1 += (26+ord(c)%32 if ord(c) < 97 else ord(c)%32 for c in keys)

    s2 = 0

    for i in range(0,len(row),3):

        first = row[i]
        second = row[i+1]
        third = row[i+2]

        f = coll.Counter(first)
        s = coll.Counter(second)
        t = coll.Counter(third)
        keys = [k for k,v in f.items() for k2,v2 in s.items() for k3,v3 in t.items() if k==k2==k3]
        s2 += sum(26+ord(c)%32 if ord(c) < 97 else ord(c)%32 for c in keys)
        print(s2)

    return s2

puzzle = Puzzle(2022, 3)

input = puzzle.input_data

solve(input)

#puzzle.answer_a = solve(input)
#puzzle.answer_b = solve(input)
