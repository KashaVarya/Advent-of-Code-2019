import sys
import copy


def halt_and_catch_fire():
    if result[0] == 19690720:
        print(100 * result[1] + result[2])
        exit()


stdin = list(map(int, sys.stdin.read().split(',')))

for i in range(0, 100):
    for j in range(0, 100):
        input_nums = copy.deepcopy(stdin)
        result = copy.deepcopy(stdin)
        result[1] = i
        result[2] = j

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
                break
