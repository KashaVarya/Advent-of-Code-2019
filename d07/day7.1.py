import sys
from itertools import permutations
from intcode_computer import IntcodeComputer


thrusters = []
perms = list(permutations(range(5), 5))
input_nums = list(map(int, sys.stdin.read().split(',')))

for perm in perms:
    out2 = 0
    for out1 in perm:
        int_comp = IntcodeComputer(input_nums[:], [out1, out2])
        out2 = int_comp.run()
        # print('out2', out2)
    thrusters.append(out2)

print(sorted(thrusters).pop())
