import sys
input = sys.stdin.readline

data = input().rstrip()

# 전부 0으로 뒤집을 때 카운트
count0 = 0
# 전부 1로 뒤집을 때 카운트
count1 = 0

# 첫 원소 값이 1일 때, 0으로 뒤집어야 하므로.
if data[0] == '1':
    count0 += 1
# 첫 원소 값이 0일 때, 1로 뒤집어야 하므로.
else:
    count1 += 1

# 첫 번째 원소값부터 돌면서
for i in range(len(data)-1):
    # 그 다음 원소값이 현재 값과 다를 때
    if data[i] != data[i+1]:
        # 다음 원소 값이 1이면
        if data[i+1] == '1':
            # 0으로 바꿔줘야 하므로.
            count0 += 1
        # 다음 원소 값이 0이면
        else:
            # 1로 바꿔줘야 하므로.
            count1 += 1

# 둘 중 최솟값 출력
print(min(count0,count1))