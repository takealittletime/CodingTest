N = int(input())

def hanoi(n,start,end,mid):
    if n == 1:
        print(start,end)
        return
    
    hanoi(n-1,start,mid,end)
    print(start,end)
    hanoi(n-1,mid,end,start)

K = 2**N - 1
print(K)
if (N <= 20):
    hanoi(N,1,3,2)