# 입력에 stdin 이용
import sys
input = sys.stdin.readline

# 수열의 크기 N, 수열 A 입력
N = int(input())
A = list(map(int, input().split()))
# 여태까지 부분 수열들의 크기 dp
dp = [1] * N
 
#  A[i]에 대해
for i in range(1, N):
    # A[j]를 비교
    for j in range(i):
        # A[j] 보다 A[i]가 크다면
        if A[i] > A[j]:
            # 부분 수열의 크기를 dp에 입력
            # but. 중복일 경우 max() 연산을 통해 방지된다.
            dp[i] = max(dp[i], dp[j]+1)
# 부분 수열 중 가장 긴 수열의 크기를 출력
print(max(dp))