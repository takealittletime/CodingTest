import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.sort(reverse=True)  # 내림차순으로 정렬

count = 0  # 초기 동전 개수를 0으로 설정
for coin in A:
    if K == 0:
        break
    
    # 현재 동전 가치로 필요한 동전의 개수 추가
    count += K // coin
    K %= coin  # 나머지 금액 갱신

print(count)
