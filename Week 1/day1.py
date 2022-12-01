from aocd.models import Puzzle

puzzle = Puzzle(2022, 1)

input_data = puzzle.input_data
input = input_data.splitlines()


counter = 0
calories = []

for i in range(len(input)):
    if(input[i] != ''):
        counter += int(input[i])
    else:
        calories.append(counter)
        counter = 0


puzzle.answer_a = max(calories)
puzzle.answer_b = (sum(sorted(calories)[-3:]))