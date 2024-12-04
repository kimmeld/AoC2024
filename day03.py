import re

# Part 1 - execute all mul() instructions
result = 0
with open("day03.input") as f:
    for l in f.readlines():
        muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)",l)
        for m in muls:
            ops = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", m).groups()
            result += int(ops[0]) * int(ops[1])
    print(f"Part 1 = {result}")

# Part 2 - execute mul() instructions only when enabled
result = 0
enabled = True
with open("day03.input") as f:
    for l in f.readlines():
        opers = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",l)
        for m in opers:
            if m == "do()":
                enabled = True
            elif m == "don't()":
                enabled = False
            elif enabled:
                ops = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", m).groups()
                result += int(ops[0]) * int(ops[1])
    print(f"Part 2 = {result}")
