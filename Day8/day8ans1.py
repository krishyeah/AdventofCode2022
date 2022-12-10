input = open("day8input.txt", "r")

grid = []

for line in input:
    grid.append(line.rstrip())

rows, cols = len(grid[0]), len(grid)

res = 0

counted = set()

# Solve looking down first (going left to right)
COL = 0
while COL < cols:
    ROW = 0
    curMax = grid[ROW][COL]
    if tuple([ROW, COL]) not in counted:
        counted.add(tuple([ROW, COL]))
        res += 1
    while ROW < rows:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
                res += 1
                counted.add(tuple([ROW, COL]))
        ROW += 1
    COL += 1

# Solve looking up next (going left to right)
COL = cols
while COL < cols:
    ROW = rows - 1
    curMax = grid[ROW][COL]
    if tuple([ROW, COL]) not in counted:
        counted.add(tuple([ROW, COL]))
        res += 1
    while ROW >= 0:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
                res += 1
                counted.add(tuple([ROW, COL]))
        ROW -= 1
    COL += 1

# Solve looking right (going top to bottom)
ROW = 0
while ROW < rows:
    COL = 0
    curMax = grid[ROW][COL]
    if tuple([ROW, COL]) not in counted:
        counted.add(tuple([ROW, COL]))
        res += 1
    while COL < cols:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
                res += 1
                counted.add(tuple([ROW, COL]))
        COL += 1
    ROW += 1

# Solve looking left (going top to bottom)
ROW = 0
while ROW < rows:
    COL = cols - 1
    curMax = grid[ROW][COL]
    if tuple([ROW, COL]) not in counted:
        counted.add(tuple([ROW, COL]))
        res += 1
    while COL >= 0:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
                res += 1
                counted.add(tuple([ROW, COL]))
        COL -= 1
    ROW += 1

print(res)