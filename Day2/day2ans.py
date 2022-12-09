input = open("day2input.txt", "r")

# Part1 
# A and X are Rock
# B and Y are Paper
# C and Z are Scissors
score_pt1 = 0
for line in input:
    if line[0] == 'A' and line[2] == 'X':
        # rock and tie
        score_pt1 += 1 + 3
    elif line[0] == 'A' and line[2] == 'Y':
        # paper and win
        score_pt1 += 2 + 6
    elif line[0] == 'A' and line[2] == 'Z':
        # scissors and loss
        score_pt1 += 3 + 0
    elif line[0] == 'B' and line[2] == 'X':
        # rock and loss
        score_pt1 += 1 + 0
    elif line[0] == 'B' and line[2] == 'Y':
        # paper and tie
        score_pt1 += 2 + 3
    elif line[0] == 'B' and line[2] == 'Z':
        # scissors and win
        score_pt1 += 3 + 6
    elif line[0] == 'C' and line[2] == 'X':
        # rock and win
        score_pt1 += 1 + 6
    elif line[0] == 'C' and line[2] == 'Y':
        # paper and loss
        score_pt1 += 2 + 0
    elif line[0] == 'C' and line[2] == 'Z':
        # scissors and tie
        score_pt1 += 3 + 3

print(score_pt1)

# Part 2
input = open("day2input.txt", "r")

score_pt2 = 0
for line in input:
    if line[0] == 'A' and line[2] == 'X':
        # scissors and loss
        score_pt2 += 3 + 0
    elif line[0] == 'A' and line[2] == 'Y':
        # rock and tie
        score_pt2 += 1 + 3
    elif line[0] == 'A' and line[2] == 'Z':
        # paper and win
        score_pt2 += 2 + 6
    elif line[0] == 'B' and line[2] == 'X':
        # rock and loss
        score_pt2 += 1 + 0
    elif line[0] == 'B' and line[2] == 'Y':
        # paper and tie
        score_pt2 += 2 + 3
    elif line[0] == 'B' and line[2] == 'Z':
        # scissors and win
        score_pt2 += 3 + 6
    elif line[0] == 'C' and line[2] == 'X':
        # paper and loss
        score_pt2 += 2 + 0
    elif line[0] == 'C' and line[2] == 'Y':
        # scissor and tie
        score_pt2 += 3 + 3
    elif line[0] == 'C' and line[2] == 'Z':
        # rock and win
        score_pt2 += 1 + 6

print(score_pt2)