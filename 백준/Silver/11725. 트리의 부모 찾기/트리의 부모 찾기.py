import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DFS 함수
def dfs(node, parent):
    # 현재 노드의 부모를 기록
    parents[node] = parent
    # 자식 노드 탐색
    for child in graph[node]:
        if parents[child] == 0:  # 아직 방문하지 않은 노드라면
            dfs(child, node)

# 입력 처리
N = int(input().rstrip())  # 노드의 개수

# 트리를 인접 리스트로 저장
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 노드의 부모를 저장할 배열
parents = [0] * (N + 1)

# DFS를 통해 부모 노드 찾기 (루트는 1)
dfs(1, -1)

# 2번 노드부터 부모 출력
for i in range(2, N + 1):
    print(parents[i])
