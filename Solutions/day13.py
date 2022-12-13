from functools import cmp_to_key
from aocd.models import Puzzle


def compare(pl, pr):
    if isinstance(pl, int) and isinstance(pr, int):
        if pl < pr:
            return -1
        elif pl == pr:
            return 0
        else:
            return 1
    elif isinstance(pl, list) and isinstance(pr, list):
        index = 0
        while index < len(pl) and index < len(pr):
            res = compare(pl[index], pr[index])
            if res == -1:
                return -1
            elif res == 1:
                return 1
            index += 1
        if index == len(pl) and index < len(pr):
            return -1
        elif index < len(pl) and index == len(pr):
            return 1
        else:
            return 0
    elif isinstance(pl, list) and isinstance(pr, int):
        return compare(pl, [pr])
    else:
        return compare([pl], pr)


def solvep1(d):
    packets = [x for x in d.split("\n\n")]
    score = 0

    for i, packet in enumerate(packets):
        pl, pr = packet.split("\n")
        pl = eval(pl)
        pr = eval(pr)
        if (compare(pl, pr)) == -1:
            score += 1 + i
        print(score)

    return score


def solvep2(d):
    packets = [x for x in d.split("\n\n")]
    packets_list = []

    for _, packet in enumerate(packets):
        pl, pr = packet.split("\n")
        pl = eval(pl)
        pr = eval(pr)
        packets_list.append(pl)
        packets_list.append(pr)

    packets_list.append([[2]])
    packets_list.append([[6]])

    packets = sorted(packets_list,
                     key=cmp_to_key(lambda pl, pr: compare(pl, pr)))
    score2 = 1

    score2 *= packets.index([[2]]) + 1
    score2 *= packets.index([[6]]) + 1
    print(score2)

    return score2


puzzle = Puzzle(2022, 13)

input = puzzle.input_data

print("Answer problem 1:", solvep1(input))
print("Answer problem 2", solvep2(input))
