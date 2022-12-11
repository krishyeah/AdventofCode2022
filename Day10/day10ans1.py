def signal_strength_calc(cycle: int, reg_x: int, res: int) -> int:
    '''Returns the signal strength addend based on provided formula.'''
    # use special signal strength formula
    if cycle == 20:
        return cycle * reg_x
    elif cycle == 60:
        return cycle * reg_x
    elif cycle == 100:
        return cycle * reg_x
    elif cycle == 140:
        return cycle * reg_x
    elif cycle == 180:
        return cycle * reg_x
    elif cycle == 220:
        return cycle * reg_x
    else:
        return 0

# read instructions from input file
instructions = open("day10input.txt", "r")

# create answer variable
res = 0
cycle = 0
reg_x = 1
# loop through all instructions
for instruction in instructions:
    # increment cycle for reading instruction
    cycle += 1
    # use special signal strength formula
    res += signal_strength_calc(cycle, reg_x, res)

    if 'addx' in instruction:
        _, count = instruction.split()
        count = int(count)
        # increment cycle for executing instruction
        cycle += 1
        # use special signal strength formula
        res += signal_strength_calc(cycle, reg_x, res)
        # add to reg_x the current value
        reg_x += count
    elif 'noop' in instruction:
        continue
    
print(res)