import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    # 시작 노드의 거리를 0으로 설정하고, 우선순위 큐에 추가
    distance[start] = 0
    heapq.heappush(q, (0, start))  # (거리, 노드) 형태로 큐에 삽입

    # 큐에 값이 있는 동안 반복
    while q:
        # 거리, 현재노드값 큐에서 꺼냄
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드들 확인
        for g in graph[now]:
            cost = dist + g[1]  # 현재 노드를 거쳐서 가는 비용
            if cost < distance[g[0]]:  # 더 짧은 경로가 발견되면 갱신
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))  # 갱신된 정보를 큐에 삽입

# 도시 수 N, 버스 수 M 입력
N = int(input())
M = int(input())

# 그래프 초기화 (도시 번호가 1부터 시작하므로 N+1)
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
q = []

# 버스 정보 입력
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 출발점, 도착점 입력
start, dest = map(int, input().split())

# 다익스트라 알고리즘 실행
dijkstra(start)

# 최소 비용 출력
print(distance[dest])
