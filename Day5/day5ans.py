# Part 1

infile = open("day5input.txt","r")

input = infile.read()

crates, moves = input.split("\n\n")
# print(crates)

crates, moves = crates.splitlines(), moves.splitlines()
# print(crates)

newstacks = [""] * 9
# print(newstacks)

for row in range(len(crates)-2, -1, -1):
    for col in range(1, len(crates[0]), 4):
        if crates[row][col].isupper():
            newstacks[col//4] += crates[row][col]

# print(newstacks)

for move in moves:
    _, crates_to_move, _, col_from, _, col_to = move.split()
    # print(crates_to_move)
    crates_to_move, col_from, col_to = int(crates_to_move), int(col_from), int(col_to)

    # Need to make them start from 0
    col_from -= 1
    col_to -= 1

    for _ in range(crates_to_move):
        newstacks[col_to] += newstacks[col_from][-1]
        newstacks[col_from] = newstacks[col_from][:-1]

# print(newstacks)
part1ans = ""
for col in range(len(newstacks)):
    part1ans += newstacks[col][-1]

print(part1ans)

# Part 2

infile = open("day5input.txt","r")

input = infile.read()

crates, moves = input.split("\n\n")
# print(crates)

crates, moves = crates.splitlines(), moves.splitlines()
# print(crates)

newstacks_pt2 = [""] * 9
# print(newstacks)

for row in range(len(crates)-2, -1, -1):
    for col in range(1, len(crates[0]), 4):
        if crates[row][col].isupper():
            newstacks_pt2[col//4] += crates[row][col]

# print(newstacks)

for move in moves:
    _, crates_to_move, _, col_from, _, col_to = move.split()
    # print(crates_to_move)
    crates_to_move, col_from, col_to = int(crates_to_move), int(col_from), int(col_to)

    # Need to make them start from 0
    col_from -= 1
    col_to -= 1

    newstacks_pt2[col_to] += newstacks_pt2[col_from][-crates_to_move:]
    newstacks_pt2[col_from] = newstacks_pt2[col_from][:-crates_to_move]

# print(newstacks_pt2)
part2ans = ""
for col in range(len(newstacks_pt2)):
    part2ans += newstacks_pt2[col][-1]

print(part2ans)