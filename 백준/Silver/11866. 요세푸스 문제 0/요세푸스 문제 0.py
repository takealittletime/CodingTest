from collections import deque

def josephus(N,K):
    people = deque(range(1,N+1))
    result = []

    while people:
        people.rotate(-(K-1))
        result.append(people.popleft())
    
    return result

N, K = map(int, input().split())
print(f"<{', '.join(map(str, josephus(N,K)))}>")