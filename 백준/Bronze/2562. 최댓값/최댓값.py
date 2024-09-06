nums = []

max_num = 0
index = 0

for i in range(9):
    nums.append(int(input().strip()))
    if (i == 0):
        max_num = nums[0]

    else:
        if (max_num < nums[i]):
            max_num = nums[i]
            index = i
index += 1

print(max_num)
print(index)