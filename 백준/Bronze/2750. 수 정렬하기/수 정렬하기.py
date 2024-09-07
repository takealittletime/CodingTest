N = int(input())

nums = []

for i in range(N):
    nums.append(int(input()))

for i in range(len(nums)-1):
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = tmp

for num in nums:
    print(num)
