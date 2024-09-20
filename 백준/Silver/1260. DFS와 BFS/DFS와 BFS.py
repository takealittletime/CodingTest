# 시스템 입/출력에 sys.stdin/stdout 사용
import sys
input = sys.stdin.readline

# 깊이 우선 탐색
def dfs(V):
    # 전역변수 N, visited1 이용
    global N
    global visited1
    
    # 노드 V 출력 후 방문 처리.
    sys.stdout.write(str(V) +' ')
    visited1[V] = 1

    # 노드 V와 인접한 미방문 노드에 대해 재귀적으로 과정 반복.
    for i in range(1, N+1):
        if (graph[V][i] == 1) and (visited1[i] == 0):
            dfs(i)

# 너비 우선 탐색
def bfs(V):
    
    # 전역변수 N, visited2 이용
    global N
    global visited2

    # 노드 V를 큐에 삽입 후 방문 처리.
    queue = [V]  
    visited2[V] = 1

    # 큐에 값이 있다면 루프 반복
    while queue:
        # 방문한 노드를 큐에서 꺼내 제거.
        V = queue.pop(0)
        sys.stdout.write(str(V) +' ')

        # 노드 V와 인접한 미방문 노드를 큐에 삽입 후 방문 처리.
        for i in range(1, N+1):
            if (visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1

# 정점의 개수 N, 간선의 개수 M, 시작 노드 V 입력
N, M, V = map(int, input().split())

# 인접행렬 방식으로 그래프 표현
graph = [ [0]*(N+1) for _ in range(N+1) ]
# 그래프 입력
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 노드를 할당할 visited 리스트
visited1 = [0] * (N+1)
visited2 = visited1.copy()

# DFS, BFS 각각 실행 및 출력
dfs(V)
sys.stdout.write('\n')
bfs(V)
