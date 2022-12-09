input = open("day1input.txt", "r")

# Part 1
maxcal_pt1 = 0
cur = 0
for line in input:
    if line == "\n":
        maxcal_pt1 = max(maxcal_pt1, cur)
        cur = 0
    else:
        cur += int(line)

ans_pt1 = maxcal_pt1
print(ans_pt1)

# Part 2
input = open("day1input.txt", "r")

maxcal_pt2 = [0, 0, 0]
cur = 0
for line in input:
    if line == "\n":
        if cur > min(maxcal_pt2):
            maxcal_pt2[maxcal_pt2.index(min(maxcal_pt2))] = cur
        cur = 0
    else:
        cur += int(line)

ans_pt2  = sum(maxcal_pt2)
print(ans_pt2)