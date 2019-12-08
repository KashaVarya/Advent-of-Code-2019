import sys
from itertools import permutations
from intcode_computer2 import IntcodeComputer


thrusters = []
perms = list(permutations(range(5, 10), 5))
input_nums = list(map(int, sys.stdin.read().split(',')))

for perm in perms:
    out2 = 0
    dontHalt = True

    int_comps = [IntcodeComputer(input_nums[:], perm[i]) for i in range(5)]

    while dontHalt:
        for i in range(len(perm)):
            out2, dontHalt = int_comps[i].run(out2)

    thrusters.append(out2)

print(sorted(thrusters).pop())
