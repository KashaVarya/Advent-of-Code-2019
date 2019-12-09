class IntcodeComputer:

    def __init__(self, input_nums, phase=False):
        self.input_nums = input_nums
        self.output = None
        self.i = 0
        self.rel_base = 0
        self.phase = phase

    def halt_and_catch_fire(self):
        return self.output, False

    def run(self, inps):
        while True:
            multiply = self.input_nums[self.i]
            self.i += 1
            multiply = str(multiply).rjust(5, '0')

            optcode = int(multiply[3:])
            mode_1 = int(multiply[2])
            mode_2 = int(multiply[1])
            mode_3 = int(multiply[0])

            if optcode == 99:
                return self.halt_and_catch_fire()
            else:
                par1 = self.input_nums[self.i]
                self.i += 1
                if mode_1 == 2:
                    par1 = self.rel_base + par1

                if optcode == 3:
                    self.input_nums[par1] = self.phase if self.phase else inps
                    self.phase = False
                elif optcode == 4:
                    self.output = self.input_nums[par1]
                    return self.output, True
                elif optcode == 9:
                    if mode_1 == 1:
                        self.rel_base += par1
                    else:
                        self.rel_base += self.input_nums[par1]
                else:
                    par2 = self.input_nums[self.i]
                    self.i += 1
                    if mode_1 != 1:
                        par1 = self.input_nums[par1]
                    if mode_2 == 0:
                        par2 = self.input_nums[par2]
                    elif mode_2 == 2:
                        par2 = self.input_nums[self.rel_base + par2]

                    if optcode == 5:
                        if par1:
                            self.i = par2
                    elif optcode == 6:
                        if not par1:
                            self.i = par2
                    else:
                        par3 = self.input_nums[self.i]
                        self.i += 1
                        if mode_3 == 2:
                            par3 += self.rel_base

                        if optcode == 7:
                            self.input_nums[par3] = 1 if par1 < par2 else 0
                        elif optcode == 8:
                            self.input_nums[par3] = 1 if par1 == par2 else 0
                        elif optcode == 1:
                            self.input_nums[par3] = par1 + par2
                        elif optcode == 2:
                            self.input_nums[par3] = par1 * par2
                        else:
                            print('Something went wrong...')
                            break
