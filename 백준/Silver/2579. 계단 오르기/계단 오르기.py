import sys
input = sys.stdin.readline

N = int(input())

steps = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
    steps[i] = int(input())

if N == 1:
    print(steps[1])
    exit()

elif N == 2:
    print(steps[1]+steps[2])
    exit()

dp[1] = steps[1]
dp[2] = steps[1] + steps[2]

for i in range(3,N+1):
    dp[i] = max(dp[i-2]+steps[i], dp[i-3]+steps[i-1]+steps[i])

print(dp[-1])