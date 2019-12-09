import sys
from intcode_computer1 import IntcodeComputer
import time


input_nums = list(map(int, sys.stdin.read().split(',')))
input_nums += [0] * 100000

int_comp = IntcodeComputer(input_nums[:])
dontHalt = True

while dontHalt:
    out, dontHalt = int_comp.run(1)
    print(out)
