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
    s = []
   
    #Forgot to cast it to an int so wasted 20 minutes+ zzzzzz
    nums = [[[int(r) for r in x.split("-")] for x in l.split(",")] for l in d.split("\n")]
    elves = 0

    for i in range(len(nums)):
        if nums[i][0][0] <= nums[i][1][0] and nums[i][0][1] >= nums[i][1][1]:
            elves+=1
        elif nums[i][1][0] <= nums[i][0][0] and nums[i][1][1] >= nums[i][0][1]:
            elves+=1
    
    s.append(elves)
    elves = 0

    for i in range(len(nums)):
        if nums[i][0][0] <= nums[i][1][1] and nums[i][0][1] >= nums[i][1][0]:
            elves+=1
        elif nums[i][1][0] <= nums[i][0][1] and nums[i][1][1] >= nums[i][0][0]:
            elves+=1
    s.append(elves)

    return s

puzzle = Puzzle(2022, 4)

input = puzzle.input_data
print(solve(input))


puzzle.answer_a = solve(input[0])
puzzle.answer_b = solve(input[1])
