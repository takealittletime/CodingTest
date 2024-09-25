import sys
input = sys.stdin.readline

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent,rank,x,y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = parent[rootX]
        elif rank[rootY] > rank[rootX]:
            parent[rootX] = parent[rootY]
        else:
            parent[rootY] = parent[rootX]
            rank[rootX] += 1

def kruskal(V, edges):
    mst_weight = 0
    mst_edges = 0

    parent = [i for i in range(V+1)]
    rank = [0]*(V+1)
    edges.sort(key=lambda x:x[2])

    for u,v,w in edges:

        if find(parent,u) != find(parent,v):
            union(parent,rank,u,v)
            mst_weight += w
            mst_edges += 1
            if mst_edges == V-1:
                break

    return mst_weight

V, E = map(int,input().split())
edges = []
for i in range(E):
    A, B, C = map(int,input().split())
    edges.append((A,B,C))

result = kruskal(V, edges)
print(result)