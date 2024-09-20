import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(parents, x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(parents, rank, x, y):
    rootX = find(parents, x)
    rootY = find(parents, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parents[rootY] = parents[rootX]
        
        elif rank[rootY] > rank[rootX]:
            parents[rootX] = parents[rootY]
        
        else:
            parents[rootY] = parents[rootX]
            rank[rootX] += 1

# 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())

# union-find에서 사용할 리스트들
parents = [i for i in range(N+1)] #부모 자식 관계 표현
rank = [0] * (N+1) #노드의 높이 표현


# 그래프 입력
for i in range(M):
    u, v = map(int, input().split())
    union(parents, rank, u,v)

# 각 노드의 루트 노드 찾기
connected_components = set(find(parents, i) for i in range(1, N+1))

print(str(len(connected_components)) + '\n')

