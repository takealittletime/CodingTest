import sys
input = sys.stdin.readline

n = int(input())
# 입력의 최댓값 (1 ≤ N ≤ 1,000,000)
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for k in range(3, n+1):
    dp[k] = (dp[k-1]+dp[k-2]) % 15746
print(dp[n])