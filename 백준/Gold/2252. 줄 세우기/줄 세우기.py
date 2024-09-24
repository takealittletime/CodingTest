import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    indegree[B] += 1

def topology_sort(N):
    result = []
    q = deque()

    # 진입차수가 0인 노드들을 모두 큐에 할당
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        current = q.popleft()
        result.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
        
    for res in result:
        print(res, end=' ')

topology_sort(N)