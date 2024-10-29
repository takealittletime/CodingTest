import sys
input = sys.stdin.readline
MAX = sys.maxsize

N, M = map(int,input().split())
users = [[MAX]*(N+1) for _ in range(N+1)]
kevin = [0]*(N+1)

for _ in range(M):
    A, B = map(int,input().split())
    users[A][B] = users[B][A] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            users[i][j] = min(users[i][j], users[i][k] + users[k][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        if users[i][j] != MAX:
            kevin[i] += users[i][j]

kevin[0] = MAX
print(kevin.index(min(kevin)))