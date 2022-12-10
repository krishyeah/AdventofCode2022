input = open("day6input.txt", "r").read()

LEFT, RIGHT = 0, 4

while RIGHT < len(input):
    curset = set(input[LEFT:RIGHT])
    # print(curset)
    if len(curset) == 4:
        print(RIGHT)
        break
    LEFT += 1
    RIGHT += 1