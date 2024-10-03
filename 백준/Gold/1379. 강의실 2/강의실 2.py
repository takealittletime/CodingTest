import sys
import heapq

input = sys.stdin.readline

# 강의 개수 입력
N = int(input())

# 강의 정보를 저장할 리스트
lectures = []
for _ in range(N):
    n, s, e = map(int, input().split())
    lectures.append((s, e, n))  # 시작 시간, 종료 시간, 강의 번호 순으로 저장

# 시작 시간을 기준으로 정렬
lectures.sort()

# 우선순위 큐 (강의실 종료 시간을 저장)
room_queue = []
# 강의실 번호를 저장할 리스트
room_assignment = [0] * (N + 1)

# 강의실 번호를 관리하는 변수
room_count = 0

for s, e, n in lectures:
    # 가장 빨리 끝나는 강의실이 현재 강의 시작 시간보다 먼저 끝나면 재사용 가능
    if room_queue and room_queue[0][0] <= s:
        end_time, room_number = heapq.heappop(room_queue)
    else:
        # 새로운 강의실 추가
        room_count += 1
        room_number = room_count

    # 강의실 배정
    room_assignment[n] = room_number
    # 현재 강의가 끝나는 시간과 강의실 번호를 우선순위 큐에 삽입
    heapq.heappush(room_queue, (e, room_number))

# 필요한 최소 강의실 수 출력
print(room_count)

# 각 강의에 배정된 강의실 번호 출력
for i in range(1, N + 1):
    print(room_assignment[i])
