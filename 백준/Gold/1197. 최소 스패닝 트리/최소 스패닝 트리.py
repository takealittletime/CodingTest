import sys
input = sys.stdin.readline

def find(x):
    global parent

    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x,y):

    global parent
    global rank

    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = parent[rootX]
        elif rank[rootY] > rank[rootX]:
            parent[rootX] = parent[rootY]
        else:
            parent[rootY] = parent[rootX]
            rank[rootX] += 1

def kruskal(edges):
    global V

    edges.sort(key=lambda x : x[2])
    mst_weight = 0
    mst_edges = 0

    for u,v,w in edges:
        if find(u) != find(v):
            union(u,v)
            mst_weight += w
            mst_edges += 1
        
        if mst_edges == V-1:
            break
    
    return mst_weight


V, E = map(int, input().split())
edges = []
for i in range(E):
    A, B, C = map(int,input().split())
    edges.append((A,B,C))
parent = [i for i in range(V+1)]
rank = [0]*(V+1)
result = kruskal(edges)
print(result)