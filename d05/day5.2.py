import sys


def halt_and_catch_fire():
    exit()


input_nums = list(map(int, sys.stdin.read().split(',')))
input_3 = 5
i = 0

while True:
    # print(input_nums)
    multiply = input_nums[i]
    i += 1
    multiply = str(multiply).rjust(4, '0')

    # print(multiply)
    optcode = int(multiply[2:])
    mode_1 = int(multiply[1])
    mode_2 = int(multiply[0])

    if optcode == 99:
        halt_and_catch_fire()
    else:
        par1 = input_nums[i]
        i += 1

        # print(par1)

        if optcode == 3:
            input_nums[par1] = input_3
        elif optcode == 4:
            if mode_1:
                print(par1)
            else:
                print(input_nums[par1])
        else:
            par2 = input_nums[i]
            i += 1
            # print(par2)
            par1 = par1 if mode_1 else input_nums[par1]
            par2 = par2 if mode_2 else input_nums[par2]



            if optcode == 5:
                if par1:
                    i = par2
            elif optcode == 6:
                if not par1:
                    i = par2
            else:
                par3 = input_nums[i]
                # print(par3)
                i += 1

                if optcode == 7:
                    input_nums[par3] = 1 if par1 < par2 else 0
                elif optcode == 8:
                    input_nums[par3] = 1 if par1 == par2 else 0
                elif optcode == 1:
                    input_nums[par3] = par1 + par2
                elif optcode == 2:
                    input_nums[par3] = par1 * par2
                else:
                    print('Something went wrong...')
                    break
