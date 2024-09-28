import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []

for _ in range(N):
    A.append(int(input()))
A.sort(reverse=True)

count = 0
for coin in A:
    count += K//coin
    K = K%coin

print(count)