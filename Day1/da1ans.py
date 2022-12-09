input = open("day1input.txt", "r")

maxcal = 0
cur = 0
for line in input:
    if line == "":
        maxcal = max(maxcal, cur)
        cur = 0
    cur += int(line)

print(maxcal)

