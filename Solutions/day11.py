import re
from aocd.models import Puzzle
from functools import reduce


class Monkey:
    def __init__(self, number, operation, items, test, condition):
        self.number = number
        self.operation = operation
        self.items = items
        self.test_value = test
        self.condtion = condition
        self.inspected = 0

    def op(self, item):
        return eval(self.operation.replace("old", str(item)))

    def test(self, item, monkeys):
        if item % self.test_value == 0:
            monkey = monkeys[self.condtion[0]]
        else:
            monkey = monkeys[self.condtion[1]]
        monkey.items.append(item)


def solvep1(d):
    input = [[m for m in l.split("\n")] for l in d.split("\n\n")]
    monkeys = []

    for i, data in enumerate(input):
        items = [int(j) for j in re.findall("(\d*\d)", data[1])]
        operation = data[2].split("= ")[1]
        test = int(re.findall("[0-9]+$\Z", data[3])[0])
        condition = (
            int(re.findall("[0-9]+$\Z", data[4])[0]),
            int(re.findall("[0-9]+$\Z", data[5])[0]),
        )
        monkey = Monkey(i, operation, items, test, condition)
        monkeys.append(monkey)

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspected += 1
                item = monkey.op(item) // 3
                monkey.test(item, monkeys)
                monkey.items = monkey.items[1:]

    s2 = sorted([monkey.inspected for monkey in monkeys])[-2:]
    return s2[0] * s2[1]


def solvep2(d):
    input = [[m for m in l.split("\n")] for l in d.split("\n\n")]
    monkeys = []

    for i, data in enumerate(input):
        items = [int(j) for j in re.findall("(\d*\d)", data[1])]
        operation = data[2].split("= ")[1]
        test = int(re.findall("[0-9]+$\Z", data[3])[0])
        condition = (
            int(re.findall("[0-9]+$\Z", data[4])[0]),
            int(re.findall("[0-9]+$\Z", data[5])[0]),
        )
        monkey = Monkey(i, operation, items, test, condition)
        monkeys.append(monkey)

    dividers = [monkey.test_value for monkey in monkeys]
    multiple = reduce((lambda x, y: x * y), dividers)

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspected += 1
                item = monkey.op(item) % multiple
                monkey.test(item, monkeys)
                monkey.items = monkey.items[1:]

    s2 = sorted([monkey.inspected for monkey in monkeys])[-2:]

    return s2[0] * s2[1]


puzzle = Puzzle(2022, 11)
input = puzzle.input_data

print("Answer problem 1:", solvep1(input))
print("Answer problem 2", solvep2(input))
