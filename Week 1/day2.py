from aocd.models import Puzzle

#puzzle = Puzzle(2022, 2)

#input_data = puzzle.input_data
score = 0
score2 = 0

with open("input.txt", "r") as f:
    for lines in f.readlines():
        round = lines[:-1].split(" ")
        score += {"X":{"A":4,"B":1,"C":7},"Y":{"A":8,"B":5,"C":2},"Z":{"A":3,"B":9,"C":6}}[round[1]][round[0]]
        score2 += {"X":{"A":3,"B":1,"C":2},"Y":{"A":4,"B":5,"C":6},"Z":{"A":8,"B":9,"C":7}}[round[1]][round[0]]


print(score,score2)

#puzzle.answer_a = 
#puzzle.answer_b = 