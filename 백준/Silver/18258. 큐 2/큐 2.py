import sys
from collections import deque

# 입력을 빠르게 받기 위해 sys.stdin.read 사용
input = sys.stdin.read
data = input().splitlines()

# deque를 사용해 큐를 구현
queue = deque()

# 출력 결과를 저장할 리스트
result = []

# 명령의 수 N
N = int(data[0])

for i in range(1, N+1):
    command = data[i]
    
    if command.startswith('push'):
        # "push X" 형태로 주어지므로 X를 추출
        _, value = command.split()
        queue.append(int(value))
    
    elif command == 'pop':
        # 큐가 비어있으면 -1 출력
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    
    elif command == 'size':
        result.append(len(queue))
    
    elif command == 'empty':
        result.append(0 if queue else 1)
    
    elif command == 'front':
        # 큐가 비어있으면 -1 출력
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)
    
    elif command == 'back':
        # 큐가 비어있으면 -1 출력
        if queue:
            result.append(queue[-1])
        else:
            result.append(-1)

# 최종 결과를 출력
sys.stdout.write('\n'.join(map(str, result)) + '\n')
