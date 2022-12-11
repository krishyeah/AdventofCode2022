def is_connected(head_pos: list[int], tail_pos: list[int]) -> bool:
    '''Check if head is connected to the tail by using absolute difference of positions.
    Returns boolean.'''
    if abs(head_pos[0] - tail_pos[0]) <= 1 and abs(head_pos[1] - tail_pos[1]) <= 1:
        return True
    else:
        return False

def move_tail(head_pos: list[int], tail_pos: list[int]) -> None:
    '''Moves tail when called. Shifts tail position one unit towards head.'''
    if head_pos[0] > tail_pos[0]:
        tail_pos[0] += 1
    if head_pos[0] < tail_pos[0]:
        tail_pos[0] -= 1
    if head_pos[1] > tail_pos[1]:
        tail_pos[1] += 1
    if head_pos[1] < tail_pos[1]:
        tail_pos[1] -= 1

moves = open("day9input.txt", "r")
# Result of which squares have been visited
res = set()

# Starting head position
head_pos = [0,0]
# Starting tail position
tail_pos = [0,0]
# Add starting position to set
res.add(tuple(tail_pos))
# Iterate through all moves
for move in moves:
    # Get direction and count of steps for each move
    dir, count = move.split()
    count = int(count)
    # print(dir)
    # print(count)

    # head moves up
    if dir == 'U':
        for _ in range(count):
            # increment head movement
            head_pos[1] += 1
            # move tail if needed
            if not is_connected(head_pos, tail_pos):
                move_tail(head_pos, tail_pos)
                # add tail position to result
                res.add(tuple(tail_pos))
    # head moves down
    elif dir == 'D':
        for _ in range(count):
            # increment head movement
            head_pos[1] -= 1
            # move tail if needed
            if not is_connected(head_pos, tail_pos):
                move_tail(head_pos, tail_pos)
                # add tail position to result
                res.add(tuple(tail_pos))
    # head moves left
    elif dir == 'L':
        for _ in range(count):
            # increment head movement
            head_pos[0] -= 1
            # move tail if needed
            if not is_connected(head_pos, tail_pos):
                move_tail(head_pos, tail_pos)
                # add tail position to result
                res.add(tuple(tail_pos))
    # head moves right
    elif dir == 'R':
        for _ in range(count):
            # increment head movement
            head_pos[0] += 1
            # move tail if needed
            if not is_connected(head_pos, tail_pos):
                move_tail(head_pos, tail_pos)
                # add tail position to result
                res.add(tuple(tail_pos))

print(len(res))