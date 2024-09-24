import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x,y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    sea += 1
                elif graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x,y,sea))
    
    for x,y,sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

ice = []
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            ice.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

year = 0

while ice:
    visited = [[0]*M for _ in range(N)]
    delList = []
    group = 0

    for i, j in ice:
        if graph[i][j] != 0 and visited[i][j] == 0:
            group += bfs(i,j)
        if graph[i][j] == 0:
            delList.append((i,j))
    
    if group >= 2:
        print(year)
        break
    # 녹은 빙하 좌표들을 리스트에서 제거.
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)