import itertools

# Load input
antenna_locs = dict()
loc_antenna = dict()
with open("day08.input") as f:
    y = 0
    for l in [l.strip() for l in f.readlines()]:
        x = 0
        for c in l:
            if c != ".":
                if c in antenna_locs:
                    antenna_locs[c].append((x,y))
                else:
                    antenna_locs[c] = [(x,y)]
                loc_antenna[(x,y)] = c
            x += 1
        y += 1
    extents = (x,y)

# Part 1
p1antinodes = set()
p2antinodes = set()
for ant in antenna_locs.keys():
    locs = antenna_locs[ant]

    for pair in itertools.permutations(locs, 2):
        # Figure out Part 1 antinode location for this pair
        a1 = pair[0]
        a2 = pair[1]
        xstep = (a1[0] - a2[0])
        ystep = (a1[1] - a2[1])

        ant_x = a1[0] + xstep
        ant_y = a1[1] + ystep
        # Is antinode in bounds?
        if ant_x >= 0 and ant_x < extents[0] and ant_y >= 0 and ant_y < extents[1]:
            p1antinodes.add((ant_x,ant_y))

        # Figure out Part 2 antinode location for this pair

        ant_x = a2[0]
        ant_y = a2[1]
        while True:
            ant_x += xstep
            ant_y += ystep

            # Is antinode in bounds?
            if ant_x >= 0 and ant_x < extents[0] and ant_y >= 0 and ant_y < extents[1]:
                p2antinodes.add((ant_x,ant_y))
            else:
                break

for y in range(0,extents[1]):
    for x in range(0, extents[0]):
        if (x,y) in loc_antenna.keys():
            print(loc_antenna[(x,y)], end="")
        else:
            print(".", end="")
    print()
print()

for y in range(0,extents[1]):
    for x in range(0, extents[0]):
        if (x,y) in p2antinodes:
            print("#", end="")
        else:
            print(".", end="")
    print()

print(f"Part 1 = {len(p1antinodes)}")
print(f"Part 2 = {len(p2antinodes)}")
# print(f"{antinodes=}")