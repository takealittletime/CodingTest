# 첫째 줄에 개수 N
N = int(input())
# 둘째 줄에 수열 A
A = list(map(int, input().split()))
# 셋째 줄에 연산자 개수 (+,-,*,/)
operators = list(map(int, input().split()))

mx = -1e9 # 식의 최댓값
mn = 1e9 # 식의 최솟값

def dfs(n, temp) :
    # 전역변수로 mx, mn 선언
    global mx, mn
    
    # 종료 조건
    if n == N-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return
     
    # 하부함수 호출
    if operators[0] != 0 : # 덧셈하는 경우
        operators[0] -= 1
        dfs(n+1, temp + A[n+1])
        operators[0] += 1 

    if operators[1] != 0 : # 뺄셈하는 경우
        operators[1]-= 1
        dfs(n+1, temp - A[n+1])
        operators[1] += 1
    
    if operators[2] != 0 : # 곱셈하는 경우
        operators[2] -= 1
        dfs(n+1, temp * A[n+1])
        operators[2] += 1
    
    if operators[3] != 0 : #나눗셈하는 경우
        operators[3] -= 1
        dfs(n+1, int(temp/A[n+1]))
        operators[3] += 1

dfs(0, A[0])
print(mx)
print(mn)