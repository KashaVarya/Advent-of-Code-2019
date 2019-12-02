import sys


def halt_and_catch_fire():
    print(result[0])


input_nums = result = list(map(int, sys.stdin.read().split(',')))
result[1] = 12
result[2] = 2

while True:
    optcode, pos1, pos2, pos3, *input_nums = input_nums

    if optcode == 1:
        result[pos3] = result[pos1] + result[pos2]
    elif optcode == 2:
        result[pos3] = result[pos1] * result[pos2]
    elif optcode == 99:
        halt_and_catch_fire()
        break
    else:
        print('Something went wrong...')
        break
