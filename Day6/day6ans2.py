input = open("day6input.txt", "r").read()

LEFT, RIGHT = 0, 4

while RIGHT < len(input):
    curset = set(input[LEFT:RIGHT])
    # print(curset)
    if len(curset) == 4:
        print(RIGHT)
        LEFT = RIGHT
        RIGHT += 14
        while RIGHT < len(input):
            curset = set(input[LEFT:RIGHT])
            if len(curset) == 14:
                print(RIGHT)
                break
            LEFT += 1
            RIGHT += 1
    LEFT += 1
    RIGHT += 1