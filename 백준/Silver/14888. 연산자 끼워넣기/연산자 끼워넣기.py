# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))

# resMax = resMin = 0
resMax = -1e9
resMin = 1e9

def dfs(n, tmp):
    global N
    global resMax
    global resMin

    if n == N-1:
        resMax = max(tmp, resMax)
        resMin = min(tmp, resMin)
        return

    if operators[0] != 0:
        operators[0] -= 1
        dfs(n+1, tmp+A[n+1])
        operators[0] += 1
    
    if operators[1] != 0:
        operators[1] -= 1
        dfs(n+1, tmp-A[n+1])
        operators[1] += 1
    
    if operators[2] != 0:
        operators[2] -= 1
        dfs(n+1, tmp * A[n+1])
        operators[2] += 1
    
    if operators[3] != 0:
        operators[3] -= 1
        dfs(n+1, int(tmp/A[n+1]))
        operators[3] += 1

dfs(0, A[0])
print(resMax)
print(resMin)