# 21606 아침산책
import sys
input = sys.stdin.readline
# print = sys.stdout.write
sys.setrecursionlimit(10**6)

# N, A 입력
N = int(input())
A = input().rstrip()

# 실내/실외 노드 여부 할당할 리스트
is_indoor = [0] * (N+1)
for i in range(len(A)):
    if A[i] == '1':
        is_indoor[i+1] = 1

# 그래프 입력
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 경로 결과, 방문 여부 할당할 리스트
result = [0] * (N+1)
visited = [0] * (N+1)

# 실외 노드에 대한 반복을 수행하는 dfs 함수
def dfs(neighbor, node):
    # (기저 조건) 인접 노드(neighbor)가 실내라면 경로 결과 추가하고 리턴
    if is_indoor[neighbor] == 1:
        result[neighbor] += 1
        result[node] += 1
        return
    
    # 인접 노드가 실외라면
    else:
        for next_neighbor in graph[neighbor]:
            if visited[next_neighbor] == 0:
                visited[next_neighbor] = 1
                dfs(next_neighbor, node)
                visited[next_neighbor] = 0 #실외 노드는 방문값 다시 0으로

for i in range(1,N+1):
    # 실내 노드 선택
    if is_indoor[i] == 1:
        visited[i] = 1 # 방문 표시
        # 인접한 노드들에 대해
        for neighbor in graph[i]:
            # 인접 노드가 실내 노드일 때
            if is_indoor[neighbor] == 1:
                # 아직 방문하지 않은 노드라면 경로 결과에 추가
                if visited[neighbor] == 0:
                    result[neighbor] += 1
                    result[i] += 1
            # 인접 노드가 실외 노드일 때
            else:
                visited[neighbor] = 1 #방문 표시
                dfs(neighbor, i)
                visited[neighbor] = 0 #실외 노드는 방문값 다시 0으로

print(sum(result))