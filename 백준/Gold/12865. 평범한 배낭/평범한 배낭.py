import sys
input = sys.stdin.readline

N, K = map(int, input().split())

items = []

for i in range(N):
    w, v = map(int, input().split())
    items.append((w,v))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w, v = items[i-1]
    for j in range(K+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# print(dp)
print(dp[N][K])