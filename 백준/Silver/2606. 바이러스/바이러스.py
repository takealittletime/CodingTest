import sys
input = sys.stdin.readline
print = sys.stdout.write

def find (parents, x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(parents,rank,x,y):
    rootX = find(parents,x)
    rootY = find(parents,y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parents[rootY] = rootX
        elif rank[rootY] > rank[rootX]:
            parents[rootX] = rootY
        else:
            parents[rootY] = rootX
            rank[rootX] += 1

C = int(input().rstrip())
N = int(input().rstrip())

parents = [i for i in range(C+1)]
rank = [0] * (C+1)

for i in range(N):
    u, v = map(int, input().split())
    union(parents,rank,u,v)

root_of_one = find(parents,1)

count = 0
for i in range(2,C+1):
    if find(parents, i) == root_of_one:
        count += 1

print(str(count)+'\n')