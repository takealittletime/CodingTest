from collections import deque
import sys
input = sys.stdin.readline

# 정점 N, 간선 M, 최단거리 K, 시작 정점 X
N, M, K, X = map(int, input().split())

# 인접 리스트 방식으로 그래프 작성
graph = [[] for _ in range(N+1)]

# 그래프 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

# BFS 함수 구현
def bfs(V, K):
    # 최단 거리를 저장할 배열 (거리 정보를 -1로 초기화)
    distance = [-1] * (N+1)
    distance[V] = 0  # 시작 도시의 거리는 0

    q = deque()
    q.append(V)

    while q:
        current = q.popleft()

        # 현재 도시에서 이동할 수 있는 모든 도시 탐색
        for next_city in graph[current]:
            if distance[next_city] == -1:  # 아직 방문하지 않은 도시라면
                distance[next_city] = distance[current] + 1
                q.append(next_city)

    # 최단 거리가 정확히 K인 도시를 오름차순으로 출력
    result = [i for i in range(1, N+1) if distance[i] == K]

    if result:
        for city in sorted(result):
            print(city)
    else:
        print(-1)

# BFS 수행
bfs(X, K)
