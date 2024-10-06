import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

result = str(A)+str(B)
result = int(result) - C

print(A+B-C)
print(result)