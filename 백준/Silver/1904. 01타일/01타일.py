import sys
input = sys.stdin.readline

def tile(n):
    if (n == 1):
        return 1
    if (n==2):
        return 2
    curr = 2
    pre = 1
    for i in range(3,n+1):
        next = (curr+pre)%15746
        pre = curr
        curr = next
    return curr

n = int(input())
print(tile(n))