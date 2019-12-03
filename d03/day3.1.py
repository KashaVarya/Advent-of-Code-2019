import sys


def make_wire(track, check=False):
    x, y = 0, 0

    for route in track:
        if 'R' in route:
            start = x + 1
            end = start + int(route[1:])
            if check:
                check_intersection(start, end, False, y)
            else:
                paint(start, end, False, y)
            x = end - 1

        elif 'L' in route:
            start = x - int(route[1:])
            end = x
            if check:
                check_intersection(start, end, False, y)
            else:
                paint(start, end, False, y)
            x = start

        elif 'U' in route:
            start = y + 1
            end = start + int(route[1:])
            if check:
                check_intersection(start, end, x, False)
            else:
                paint(start, end, x, False)
            y = end - 1

        elif 'D' in route:
            start = y - int(route[1:])
            end = y
            if check:
                check_intersection(start, end, x, False)
            else:
                paint(start, end, x, False)
            y = start


def paint(start, end, x, y):
    for i in range(start, end):
        if not x and type(x) == bool:
            wires.append((i, y))
        elif not y and type(y) == bool:
            wires.append((x, i))


def check_intersection(start, end, x, y):
    for i in range(start, end):
        if not x and type(x) == bool:
            if (i, y) in wires:
                min_dis.add(abs(i) + abs(y))
        elif not y and type(y) == bool:
            if (x, i) in wires:
                min_dis.add(abs(x) + abs(i))


line1, line2 = [line.split(',') for line in sys.stdin.read().split('\n')]

wires = []
min_dis = set()

make_wire(line1)
make_wire(line2, True)

print(sorted(min_dis)[0] if len(min_dis) else 'No intersections')
