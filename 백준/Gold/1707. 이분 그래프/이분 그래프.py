import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(node, color):
    checks[node] = color

    for neighbor in graph[node]:
        if checks[neighbor] == 0:
            if not DFS(neighbor,-color):
                return False
        elif checks[neighbor] == checks[node]:
            return False
    
    return True

K = int(input())
for _ in range(K):
    # 정점 개수 V, 간선 개수 E
    V, E = map(int, input().split())
    # 그래프를 인접 리스트 형태로 구현
    graph = [[] for _ in range(V+1)]
    # 그래프 입력
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 각 노드 별로 색깔을 할당할 리스트. (-1 또는 1로 색 표현. 0은 빈 상태를 표시.) 
    checks = [0]*(V+1)
    is_bipartite = True
    # 모든 정점에 대해 DFS 실행 (연결 그래프가 아닐 수도 있음)
    for i in range(1, V + 1):
        if checks[i] == 0:  # 방문하지 않은 노드만 탐색
            if not DFS(i, 1):
                is_bipartite = False
                break
    if (is_bipartite):
        print("YES")
    else:
        print("NO")
    