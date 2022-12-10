# Part 1
input = open("day4input.txt", "r")
part1ans = 0
for line in input:
    elfs = line.split(',')
    elf1 = elfs[0]
    elf2 = elfs[1]

    elf1_start = int(elf1.split('-')[0])
    elf1_end = int(elf1.split('-')[1])

    elf2_start = int(elf2.split('-')[0])
    elf2_end = int(elf2.split('-')[1])

    if elf1_start <= elf2_start and elf1_end >= elf2_end:
        part1ans += 1
    elif elf1_start >= elf2_start and elf1_end <= elf2_end:
        part1ans += 1

print(part1ans)

# Part 2
input = open("day4input.txt", "r")
part2ans = 0

for line in input:
    elfs = line.split(',')
    elf1 = elfs[0]
    elf2 = elfs[1]

    elf1_start = int(elf1.split('-')[0])
    elf1_end = int(elf1.split('-')[1])

    elf2_start = int(elf2.split('-')[0])
    elf2_end = int(elf2.split('-')[1])

    if elf1_start <= elf2_start and elf2_start <= elf1_end:
        part2ans += 1
    elif elf2_start <= elf1_start and elf1_start <= elf2_end:
        part2ans += 1
    elif elf2_start <= elf1_end and elf2_end >= elf1_end:
        part2ans += 1
    elif elf1_start <= elf2_end and elf1_end >= elf2_end:
        part2ans += 1
    
print(part2ans)