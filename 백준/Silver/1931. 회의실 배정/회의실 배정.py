# 입력에 stdin 사용
import sys
input = sys.stdin.readline

# N, 회의 시간 입력
N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    # 튜플 형태로 할당 (시작 시간, 종료 시간)
    meetings.append((start, end))

# 끝나는 시간을 기준으로 정렬 (끝나는 시간이 같으면 시작 시간을 기준으로 정렬)
meetings.sort(key=lambda x: (x[1], x[0]))

# 결과 할당 변수, 회의 종료 시간 할당 변수
count = 0
end_time = 0

# 반복문 안에서 종료 시간 < 회의 시작 시간인 경우마다 할당
for meeting in meetings:
    if end_time <= meeting[0]:
        end_time = meeting[1]
        count += 1
# 결과 출력
print(count)