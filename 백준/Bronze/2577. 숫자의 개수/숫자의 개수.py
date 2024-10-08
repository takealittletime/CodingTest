import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

res = str(A*B*C)
tmp = [0] * 10

for i in range(len(res)):
    tmp[int(res[i])] += 1

for result in tmp:
    print(result)