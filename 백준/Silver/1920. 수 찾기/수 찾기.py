import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.read

data = input().splitlines()
N = int(data[0])
A = list(map(int,data[1].split()))
N = int(data[2])
B = list(map(int,data[3].split()))

A.sort()

def binary_search (arr, x):
    left = bisect_left(arr,x)
    right = bisect_right(arr,x)

    return left != right

result = []
for num in B:
    if (binary_search(A,num)):
        result.append(1)
    else:
        result.append(0)

print('\n'.join(map(str,result)))