# read instructions from file
instructions = open("day10input.txt", "r")

# prepare result
res = ['\n','\n','\n','\n','\n','\n']
# cycle count
cycle = 0
# reg_x pointer
reg_x = 1

for instruction in instructions:
    # increase cycle for reading instruction
    cycle += 1
    # calculate what row is currently being printed
    ROW = (cycle-1)//40
    print(ROW)
    if abs((cycle-1) % 40 - reg_x) <= 1:
        res[ROW] += '#'
    else:
        res[ROW] += '.'
    
    if 'addx' in instruction:
        _, count = instruction.split()
        count = int(count)
        # increment cycle for executing instruction
        cycle += 1
        ROW = (cycle-1)//40
        print(ROW)
        if abs((cycle-1) % 40 - reg_x) <= 1:
            res[ROW] += '#'
        else:
            res[ROW] += '.'
        # add to reg_x the current value
        reg_x += count

print(''.join(res))