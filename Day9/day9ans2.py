def is_connected(lead_knot: list[int], trail_knot: list[int]) -> bool:
    '''Check if head is connected to the tail by using absolute difference of positions.
    Returns boolean.'''
    if abs(lead_knot[0] - trail_knot[0]) <= 1 and abs(lead_knot[1] - trail_knot[1]) <= 1:
        return True
    else:
        return False

def move_tail(lead_knot: list[int], trail_knot: list[int]) -> None:
    '''Moves rope position when called. Shifts tail position one unit towards head.'''
    if lead_knot[0] > trail_knot[0]:
        trail_knot[0] += 1
    if lead_knot[0] < trail_knot[0]:
        trail_knot[0] -= 1
    if lead_knot[1] > trail_knot[1]:
        trail_knot[1] += 1
    if lead_knot[1] < trail_knot[1]:
        trail_knot[1] -= 1

moves = open("day9input.txt", "r")
# Result of which squares have been visited
res = set()

# Starting rope position
rope_pos = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
# Head position pointer
head_pos = rope_pos[0]
# Tail position pointer
tail_pos = rope_pos[-1]
# Add starting position to set
res.add(tuple(tail_pos))
# Iterate through all moves
for move in moves:
    # Get direction and count of steps for each move
    dir, count = move.split()
    count = int(count)

    # head moves up
    if dir == 'U':
        for _ in range(count):
            # increment head position
            head_pos[1] += 1
            # make tail move in order
            for i in range(1, len(rope_pos)):
                if not is_connected(rope_pos[i-1], rope_pos[i]):
                    move_tail(rope_pos[i-1], rope_pos[i])
                else:
                    break
            # add tail position to result
            res.add(tuple(tail_pos))
    # head moves down
    elif dir == 'D':
        for _ in range(count):
            # increment head position
            head_pos[1] -= 1
            # make tail move in order
            for i in range(1, len(rope_pos)):
                if not is_connected(rope_pos[i-1], rope_pos[i]):
                    move_tail(rope_pos[i-1], rope_pos[i])
                else:
                    break
            # add tail position to result
            res.add(tuple(tail_pos))
    # head moves left
    elif dir == 'L':
        for _ in range(count):
            # increment head position
            head_pos[0] -= 1
            # make tail move in order
            for i in range(1, len(rope_pos)):
                if not is_connected(rope_pos[i-1], rope_pos[i]):
                    move_tail(rope_pos[i-1], rope_pos[i])
                else:
                    break
            # add tail position to result
            res.add(tuple(tail_pos))
    # head moves right
    elif dir == 'R':
        for _ in range(count):
            # increment head position
            head_pos[0] += 1
            # make tail move in order
            for i in range(1, len(rope_pos)):
                if not is_connected(rope_pos[i-1], rope_pos[i]):
                    move_tail(rope_pos[i-1], rope_pos[i])
                else:
                    break
            # add tail position to result
            res.add(tuple(tail_pos))

print(len(res))