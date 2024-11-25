import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellmanFord(start):
    distance[start] = 0
    # N-1번 반복
    for _ in range(N - 1):
        for curr, next, cost in bus:
            if distance[curr] != INF and distance[next] > distance[curr] + cost:
                distance[next] = distance[curr] + cost

    # N번째 반복에서 음수 사이클 확인
    for curr, next, cost in bus:
        if distance[curr] != INF and distance[next] > distance[curr] + cost:
            return False  # 음수 사이클 존재
    return True

N,M = map(int,input().split())
bus = list(tuple(map(int,input().split())) for _ in range(M))
distance = [INF] * (N+1)
if bellmanFord(1):
  for i in range(2,len(distance)):
    if distance[i] >= INF:
      print(-1)
    else:
      print(distance[i])
else:
  print(-1)