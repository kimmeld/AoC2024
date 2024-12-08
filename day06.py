# Map chars -> Direction
facing = dict()
facing['^'] = (0,-1)
facing['>'] = (1,0)
facing['v'] = (0,1)
facing['<'] = (-1,0)

# List of directions - ordered so that adding one to the index results in a right turn
directions = [(0,-1),(1,0),(0,1),(-1,0)]

# Load input
starting_grid = dict()
starting_pos = (0,0)
with open("day06.input") as f:
    y = 0
    for l in [l.strip() for l in f.readlines()]:
        x = 0
        for c in l:
            starting_grid[(x,y)] = c
            if c == "^":
                starting_pos = (x,y)
            x += 1
        y += 1
    extents = (x,y)
starting_direction = facing[starting_grid[starting_pos]]

def walk_grid(grid, start_pos, start_direction):
    pos = start_pos
    direction = start_direction
    steps_taken = set()
    while True:
        try:
            # Handle turns.  If turning results in hitting an obstacle, turn again
            for blah in range(0,4):
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                if grid[new_pos] == "#":
                    direction = directions[ (directions.index(direction) + 1) % 4 ]
                else:
                    break

            pos = (pos[0] + direction[0], pos[1] + direction[1])

            this_step = (pos, direction)
            if this_step in steps_taken:
                # We've hit an endless loop as we've already touched this square going in this direction once
                return True
            
            steps_taken.add(this_step)

            grid[pos] = 'X'
        except KeyError:
            # Guard went out of bounds
            return False

part1 = 0
p1grid = starting_grid.copy()
walk_grid(p1grid, starting_pos, starting_direction)
for c in p1grid.values():
    if c == "X":
        part1 += 1
print(f"Part 1 = {part1}")


part2 = 0
first_pos = (starting_pos[0] + starting_direction[0], starting_pos[1] + starting_direction[1])
for x in range(0,extents[0]):
    for y in range(0,extents[1]):
        # Only place an obstacle on an empty spot that is somewhere the guard will walk
        if starting_grid[(x,y)] == "." and p1grid[(x,y)] == "X":
            grid = starting_grid.copy()
            grid[(x,y)] = "#"
            # print(f"Checking {(x,y)}")
            if walk_grid(grid, starting_pos, starting_direction):
                part2 += 1
print(f"Part 2 = {part2}")