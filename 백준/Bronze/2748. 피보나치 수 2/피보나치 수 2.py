import sys
input = sys.stdin.readline

def fibo(n):
    prev = 1
    curr = 0

    for _ in range(1,n+1):
        next = curr + prev
        prev = curr
        curr = next
    return curr

n = int(input())
print(fibo(n))