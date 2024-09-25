import sys
from collections import deque
input = sys.stdin.readline

def dfs(V):
    print(V, end = ' ')
    visited1[V] = 1

    for neighbor in sorted(graph[V]):
        if not visited1[neighbor]:
            dfs(neighbor)

def bfs(V):

    q = deque([V])
    visited2[V] = 1

    while q:
        current = q.popleft()
        print(current, end=' ')
        

        for neighbor in sorted(graph[current]):
            if not visited2[neighbor]:
                q.append(neighbor)
                visited2[neighbor] = 1



N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

dfs(V)
print()
bfs(V)

# print(graph)