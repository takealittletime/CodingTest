# 입력에 stdin 사용
import sys
input = sys.stdin.readline

def dp(n):
    # n = 1 또는 2 일 때 그대로 출력
    if (n == 1) or (n == 2):
        return n
    
    # curr은 2에서, pre는 1에서 시작하며 각각 이전 값들을 저장하면서 수행
    curr = 2
    pre = 1
    for i in range(3,n+1):
        next = (curr+pre)%15746
        pre = curr
        curr = next
    return curr

# n 입력, 결과 출력
n = int(input())
print(dp(n))