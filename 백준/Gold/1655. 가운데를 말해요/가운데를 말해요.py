import sys
import heapq

input = sys.stdin.read
data = input().split()
N = int(data[0])
nums = list(map(int,data[1:]))

left = []
right = []
result = []

for i in range (N):
    num = nums[i]

    #순서 돌아가며 힙에 값 입력
    if len(left) == len(right):
        heapq.heappush(left, -num)
        heapq.heappush(right, num)
    
    # 예외 처리:: 최대힙의 루트가 최소힙의 루트보다 더 큰 경우
    if right and -left[0] > right[0]:
        left_max = -heapq.heappop(left)
        right_min = heapq.heappop(right)

        heapq.heappush(left, -right_min)
        heapq.heappush(right, left_max)
    
    result.append(-left[0])

sys.stdout.write('\n'.join(map(str,result)))