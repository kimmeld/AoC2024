# Parse input into two lists
list1 = []
list2 = []
with open("day01.input") as f:
    for l in f.readlines():
        nums = l.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
list1.sort()
list2.sort()

# Calculate the total distance and similarity between the two lists
total_dist = 0
similarity_score = 0
for l, r in zip(list1, list2):
    total_dist += abs(l-r)
    similarity_score += l * list2.count(l)

# Output results
print(f"Part 1 = {total_dist}")
print(f"Part 2 = {similarity_score}")