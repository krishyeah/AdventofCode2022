def is_connected(self, head_pos: list[int], tail_pos: list[int]) -> bool:
    '''Check if head is connected to the tail by using absolute difference of positions.
    Returns boolean.'''
    if abs(head_pos[0] - tail_pos[0]) <= 1 and abs(head_pos[1] - tail_pos[1]) <= 1:
        return True
    else:
        return False

def move_tail(self, head_pos: list[int], tail_pos: list[int]) -> None:
    '''Moves tail when called. Shifts tail position one unit towards head.'''
    tail_pos[0] += 1

moves = open("day9input.txt", "r").read()

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
    dir, count = move.split(' ')
    # head moves up
    if dir == 'U':
        head_pos[1] += 1
        if not is_connected(head_pos, tail_pos):
            move_tail(head_pos, tail_pos)
        continue
    # head moves down
    if dir == 'D':
        continue
    # head moves left
    if dir == 'L':
        continue
    # head moves right
    if dir == 'R':
        continue