import itertools

equations = []
with open("day07.input") as f:
    for l in f.readlines():
        result, numbers = l.split(":")
        numbers = numbers.split()
        equations.append( (int(result), [int(n) for n in numbers]) )

# Part 1
# Try every combination of operators to see if we can make the equation true
part1 = 0
for result, nums in equations:
    nops = len(nums) - 1
    tests = itertools.product("+*", repeat=nops)
    for test in tests:
        my_nums = nums.copy()
        my_res = my_nums.pop(0)
        for op in test:
            if op == "+":
                my_res += my_nums.pop(0)
            if op == "*":
                my_res *= my_nums.pop(0)
        if my_res == result:
            # print(f'Yay {my_res} {test}')
            part1 += result
            break
print(f"Part 1 = {part1}")


# Part 2
# Same as part 1, with a new operator
part2 = 0
for result, nums in equations:
    nops = len(nums) - 1
    tests = itertools.product("+*|", repeat=nops)
    for test in tests:
        my_nums = nums.copy()
        my_res = my_nums.pop(0)
        for op in test:
            if op == "+":
                my_res += my_nums.pop(0)
            if op == "*":
                my_res *= my_nums.pop(0)
            if op == "|":
                my_res = int(str(my_res) + str(my_nums.pop(0)))
        if my_res == result:
            # print(f'Yay {my_res} {test}')
            part2 += result
            break
print(f"Part 2 = {part2}")