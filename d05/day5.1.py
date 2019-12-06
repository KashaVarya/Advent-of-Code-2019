import sys


def halt_and_catch_fire():
    exit()


input_nums = list(map(int, sys.stdin.read().split(',')))
input_3 = 1
i = 0

while True:
    multiply = input_nums[i]
    i += 1
    multiply = str(multiply).rjust(4, '0')

    optcode = int(multiply[2:])
    mode_1 = int(multiply[1])
    mode_2 = int(multiply[0])

    if optcode == 99:
        halt_and_catch_fire()
    else:
        par1 = input_nums[i]
        i += 1

        if optcode == 3:
            input_nums[par1] = input_3
        elif optcode == 4:
            if mode_1:
                print(par1)
            else:
                print(input_nums[par1])
        else:
            par2, par3 = input_nums[i:i+2]
            i += 2
            par1 = par1 if mode_1 else input_nums[par1]
            par2 = par2 if mode_2 else input_nums[par2]

            if optcode == 1:
                input_nums[par3] = par1 + par2
            elif optcode == 2:
                input_nums[par3] = par1 * par2
            else:
                print('Something went wrong...')
                break
