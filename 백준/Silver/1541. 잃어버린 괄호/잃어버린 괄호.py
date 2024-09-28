import sys
input = sys.stdin.readline

N = input().rstrip()
# 입력에서 '-' 연산자를 기준으로 분할
M = N.split('-')

answer = sum(map(int,M[0].split('+')))

for group in M[1:]:
    answer -= sum(map(int,group.split('+')))

print(answer)
