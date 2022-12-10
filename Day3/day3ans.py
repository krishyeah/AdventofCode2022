# Part1
input = open("day3input.txt", "r")

part1ans = 0
for line in input:
    num_items = len(line)
    num_compartment = num_items//2
    # print(num_compartment)

    compartment1 = line[:num_compartment]
    compartment2 = line[num_compartment:]
    # print(compartment1)
    # print(compartment2)

    set1 = set(compartment1)
    set2 = set(compartment2)

    curItem = ''.join(set1.intersection(set2))
    if curItem.islower():
        part1ans += ord(curItem) - ord('a') + 1
    else:
        part1ans += ord(curItem) - ord('A') + 27

print(part1ans)

# Part 2
input = open("day3input.txt", "r")
part2ans = 0
lines = []
count = 0
for line in input:
    if len(lines) < 3:
        lines.append(line.rstrip())
        # print(lines)
    else:
        set1 = set(lines[0])
        set2 = set(lines[1])
        set3 = set(lines[2])
        badge = set1.intersection(set2).intersection(set3)

        # print(badge)
        badgestr = ''.join(badge)
        print(badgestr)
        if badgestr.islower():
            part2ans += ord(badgestr) - ord('a') + 1
        else:
            part2ans += ord(badgestr) - ord('A') + 27

        count += 1
        lines.clear()
        lines.append(line)
set1 = set(lines[0])
set2 = set(lines[1])
set3 = set(lines[2])
badge = set1.intersection(set2).intersection(set3)

# print(badge)
badgestr = ''.join(badge)
print(badgestr)
if badgestr.islower():
    part2ans += ord(badgestr) - ord('a') + 1
else:
    part2ans += ord(badgestr) - ord('A') + 27

count += 1
lines.clear()
lines.append(line)

print(part2ans)
