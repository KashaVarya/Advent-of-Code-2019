import sys

print(sum([int(int(mass) / 3) - 2 for mass in sys.stdin]))
