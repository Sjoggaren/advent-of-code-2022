from aocd.models import Puzzle
import itertools

puzzle = Puzzle(2017, 2)

input_data = puzzle.input_data

rows = input_data.splitlines()
rows = [[int(val) for val in row.split('\t')] for row in rows]
puzzle.answer_a = sum([max(row) - min(row) for row in rows])

puzzle.answer_b = sum(b//a for row in rows for a, b in itertools.combinations(sorted(row), 2) if b%a==0)