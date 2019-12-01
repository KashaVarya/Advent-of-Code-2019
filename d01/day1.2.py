import sys

fuels = []
for fuel in sys.stdin:
    while (fuel := int(int(fuel) / 3) - 2) > 0:
        fuels.append(fuel)

print(sum(fuels))
