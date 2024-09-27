import sys
input = sys.stdin.readline

def dfs(x,y):
    if graph[x][y] == '-':
        visited[x][y] = 1
        for i in range(2):
            ny = y + delta[i]
            if 0<=ny<M and not visited[x][ny] and graph[x][ny] == '-':
                dfs(x,ny)
    
    if graph[x][y] == '|':
        visited[x][y] = 1
        for i in range(2):
            nx = x + delta[i]
            if 0<=nx<N and not visited[nx][y] and graph[nx][y] == '|':
                dfs(nx,y)

N,M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(input().rstrip())

visited = [[0]*M for _ in range(N)]

delta = [-1,1]

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i,j)
            count += 1
print(count)