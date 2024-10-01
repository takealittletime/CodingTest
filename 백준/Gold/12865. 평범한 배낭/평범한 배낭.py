# 입력에 stdin 이용
import sys
input = sys.stdin.readline

# 물품의 수 N, 적재하중 K 입력
N, K = map(int, input().split())
# 물건들 할당할 리스트
items = []
# 물건의 무게, 가치 튜플 형식으로 할당
for i in range(N):
    w, v = map(int, input().split())
    items.append((w,v))
# 문제를 풀 2차원 리스트 선언
dp = [[0]*(K+1) for _ in range(N+1)]
# 2차원 배열을 순회하면서
for i in range(1,N+1):
    # item 리스트에서 물건의 무게, 가치값 꺼냄
    w, v = items[i-1]
    for j in range(K+1):
        # 현재 적재하중이 물건의 무게 이상일 경우 (=적재가 가능할 경우)
        if j >= w:
            # dp[i-1][j-w] + v, dp[i-1][j] 값 중 큰 값으로 채운다.
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        # 이외의 값은 윗 줄의 값을 그대로 긁어 내려온다.
        else:
            dp[i][j] = dp[i-1][j]
# 결과 출력
print(dp[N][K])