# Part One: Day 1
# Read input
with open("input.txt") as f:
    data = f.read().splitlines()

# Make groups
group_number = 0
groups = []
group_to_add = []
for i in range(len(data)):
    if data[i] == "":
        group_number += 1
        groups.append(group_to_add)
        group_to_add = []
    else:
        group_to_add.append(int(data[i]))

# Find the sum of the group with the highest sum
highest_sum = 0
for group in groups:
    if sum(group) > highest_sum:
        highest_sum = sum(group)

print(highest_sum)

# Part Two: Day 1
# Calculate the sum of every group
sums = [sum(group) for group in groups]
# Sort in descending order
sums.sort(reverse=True)
# Sum the top three sums
print(sums[0] + sums[1] + sums[2])
