rules = []
data = []

reading_rules = True
with open("day05.input") as f:
    for l in f.readlines():
        l = l.strip()
        if l == "":
            reading_rules = False
            continue
        if reading_rules:
            parts = l.split("|")
            rule = (int(parts[0]), int(parts[1]))
            rules.append(rule)
        else:
            parts = [int(x) for x in l.split(',')]
            data.append(parts)

part1 = 0
part2 = 0
for item in data:
    bad = False
    for rule in rules:
        if rule[0] in item and rule[1] in item:
            # This is the inverse of what the rule means, we're looking for a rule that is violated
            if item.index(rule[0]) > item.index(rule[1]):
                bad = True
    if not bad:
        middleval = item[len(item) // 2]
        part1 += middleval

    if bad:
        # Fix it according to the page ordering rules
        # Every time we see a rule violation, we swap the two elements which are in violation
        # doing this until we don't have anything to swap results in a correctly-ordered list!
        # It's basically bubble sort but with a weird comparison operator!
        while True:
            bad = False
            for rule in rules:
                if rule[0] in item and rule[1] in item:
                    i1 = item.index(rule[0])
                    i2 = item.index(rule[1])
                    if i1 > i2:
                        item[i1], item[i2] = item[i2], item[i1]
                        bad = True
            if not bad:
                middleval = item[len(item) // 2]
                part2 += middleval
                break

print(f"Part 1 = {part1}")
print(f"Part 2 = {part2}")