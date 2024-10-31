import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellmanFord():
    for i in range(N):
        for j in range(len(edges)):
            curr, next, cost = edges[j]
            if distance[next]>distance[curr]+cost:
                distance[next] = distance[curr] + cost
                if i == N-1:
                    return True
    return False

TC = int(input())

for _ in range(TC):
    N, M, W = map(int,input().split())
    distance = [INF]*(N+1)
    edges = []

    # 도로 입력
    for _ in range(M):
        S, E, T = map(int,input().split())
        # 도로는 양방향 입력
        edges.append((S,E,T))
        edges.append((E,S,T))
    # 웜홀 입력
    for _ in range(W):
        S, E, T = map(int,input().split())
        # 웜홀은 단방향 입력
        edges.append((S,E,(-T)))
    
    if bellmanFord():
        print("YES")
    else:
        print("NO")