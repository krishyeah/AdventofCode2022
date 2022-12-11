input = open("day8input.txt", "r")

grid = []

for line in input:
    grid.append(line.rstrip())

rows, cols = len(grid[0]), len(grid)

counted = set()

# Solve looking down first (going left to right)
COL = 0
while COL < cols:
    ROW = 0
    curMax = grid[ROW][COL]
    if tuple([ROW, COL]) not in counted:
        counted.add(tuple([ROW, COL]))
    while ROW < rows:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
                counted.add(tuple([ROW, COL]))
        ROW += 1
    COL += 1

# Solve looking up next (going left to right)
COL = 0
while COL < cols:
    ROW = rows - 1
    curMax = grid[ROW][COL]
    if tuple([ROW, COL]) not in counted:
        counted.add(tuple([ROW, COL]))
    while ROW >= 0:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
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
    while COL < cols:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
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
    while COL >= 0:
        if grid[ROW][COL] > curMax:
            curMax = grid[ROW][COL]
            if tuple([ROW, COL]) not in counted:
                counted.add(tuple([ROW, COL]))
        COL -= 1
    ROW += 1

max_sight = 0

for tree in counted:
    treeRow = tree[0]
    treeCol = tree[1]
    # Look up
    ROW = tree[0] - 1
    COL = tree[1]
    up_sight = 0
    while ROW >= 0:
        up_sight += 1
        if grid[treeRow][treeCol] > grid[ROW][COL]:
            ROW -= 1
        else:
            break
    if up_sight == 0:
        continue

    # Look down
    ROW = tree[0] + 1
    COL = tree[1]
    down_sight = 0
    while ROW < rows:
        down_sight += 1
        if grid[treeRow][treeCol] > grid[ROW][COL]:
            ROW += 1
        else:
            break
    if down_sight == 0:
        continue

    # Look right
    ROW = tree[0]
    COL = tree[1] + 1
    right_sight = 0
    while COL < cols:
        right_sight += 1
        if grid[treeRow][treeCol] > grid[ROW][COL]:
            COL += 1
        else:
            break
    if right_sight == 0:
        continue

    # Look left
    ROW = tree[0]
    COL = tree[1] - 1
    left_sight = 0
    while COL >= 0:
        left_sight += 1
        if grid[treeRow][treeCol] > grid[ROW][COL]:
            COL -= 1
        else:
            break
    if left_sight == 0:
        continue
    cur_sight = up_sight * down_sight * left_sight * right_sight
    max_sight = max(max_sight, cur_sight)

print(max_sight)