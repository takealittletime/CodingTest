# def find_recur(parent,x):
#     if x != parent[x]:
#         find_recur(parent,parent[x])
#     return parent[x]

def find(parent, x):
    while parent[x] != x:
        # 경로 압축: 부모를 할당
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x    

def union(parent, rank, x, y):
    rootX = find(parent,x)
    rootY = find(parent,y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def kruskal(V, edges):

    # 부모 노드
    parent = [i for i in range(V+1)]
    # 트리 높이
    rank = [0] * (V+1)
    # 가중치를 기준으로 간선 오름차순 정렬
    edges.sort(key=lambda x:x[2])
    mst_weight = 0
    mst_edges = 0

    for u,v,w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += w
            mst_edges += 1

            if mst_edges == V - 1:
                break
    
    return mst_weight



V, E = map(int, input().split())
edges = []

for i in range(E):
    A,B,C = map(int,input().split())
    edges.append((A,B,C))

print(kruskal(V,edges))