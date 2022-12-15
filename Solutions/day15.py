from aocd.models import Puzzle


def smaller(x, y, S):
    for (sx, sy, d) in S:
        dnew = abs(x - sx) + abs(y - sy)
        if dnew <= d:
            return True
    return False


def solvep1(d):
    row = [x for x in d.split("\n")]
    sensors = set()
    beacons = set()

    for line in row:
        elem = line.split()
        sx, sy = elem[2], elem[3]
        bx, by = elem[8], elem[9]
        sx = int(sx[2:-1])
        sy = int(sy[2:-1])
        bx = int(bx[2:-1])
        by = int(by[2:])
        d = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, d))
        beacons.add((bx, by))

    closer = 0

    for x in range(-5000000, 5000000):
        y = 2000000
        if smaller(x, y, sensors) and (x, y) not in beacons:
            closer += 1

    return closer


def find_distress_beacon(sensors):
    for sx, sy, d in sensors:
        for p in range(d + 1):
            for x, y in (
                (sx - d - 1 + p, sy - p),
                (sx + d + 1 - p, sy - p),
                (sx - d - 1 + p, sy + p),
                (sx + d + 1 - p, sy + p),
            ):
                if 0 <= x <= 4000000 and 0 <= y <= 4000000:
                    further = [abs(x - nx) + abs(y - ny) > nd for nx, ny, nd in sensors]
                    if all(further):
                        return (x * 4000000 + y)


def solvep2(d):
    row = [x for x in d.split("\n")]
    sensors = set()
    beacons = set()

    for line in row:
        elem = line.split()
        sx, sy = elem[2], elem[3]
        bx, by = elem[8], elem[9]
        sx = int(sx[2:-1])
        sy = int(sy[2:-1])
        bx = int(bx[2:-1])
        by = int(by[2:])
        d = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, d))
        beacons.add((bx, by))

    return find_distress_beacon(sensors)


puzzle = Puzzle(2022, 15)
input = puzzle.input_data

print("Answer problem 1:", solvep1(input))
print("Answer problem 2:", solvep2(input))
