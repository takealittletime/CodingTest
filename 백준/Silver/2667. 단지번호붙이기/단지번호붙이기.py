# 2667. 단지번호붙이기
# deque 이용, 입력에 stdin 이용
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    total = 0   # 단지 내 집의 수
    # 큐에 좌표 할당
    q = deque([(x,y)])
    

    # 큐가 존재하는 동안 반복
    while q:
        # 큐에서 값 꺼내 방문처리
        x,y = q.popleft()
        visited[x][y] = 1
        total += 1 

        # 네 방향 이동처리
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 다음 좌표가 유효할 때
            if 0<=nx<N and 0<=ny<N:
                # 미방문한 집이 있다면 큐에 추가.
                if graph[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append(((nx,ny)))
                    # 단지내 집의 수 카운트
                    
    # 단지 내 집의 수 리턴.
    return total

# N 입력
N = int(input())

# 그래프 인접행렬로 구현
graph = [ input().rstrip() for _ in range(N)]
# 방문 여부 리스트
visited = [[0]*(N) for _ in range(N)]

# 4방향 이동 구현을 위한 dx, dy
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 총 단지 수, 단지 내 집의 수
results = []

# 그래프 내 미방문한 집(1)에 대해서 bfs 수행
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            results.append(bfs(i,j))
            # 단지 수 카운트

# 결과 출력 (총 단지 수, 단지 내 집의 수)
print(len(results))
for result in sorted(results):
    print(result)