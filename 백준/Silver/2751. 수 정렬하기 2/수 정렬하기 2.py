import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = []

for i in range(N):
    nums.append(int(input().rstrip()))

nums.sort()

for num in nums:
    print(num)