import sys
import math

def eratos(n):
    primes = [True] * (n+1)
    primes[0],primes[1] = False, False

    for i in range(2,int(math.sqrt(n))+1):
        if primes[i]:
            for j in range (i*i, n+1, i):
                primes[j] = False
    
    return [i for i in range(2,n+1) if primes[i]]

def find_goldbach(n, primes):
    for a in range( n//2, 1, -1):
        b = n-a

        if a in primes and b in primes:
            return [a,b]


input = sys.stdin.readline

primes = eratos(10000)

T = int(input().rstrip())
for i in range (T):
    n = int(input().rstrip())
    result = find_goldbach(n, primes)

    if result:
        result.sort()
        print(f"{result[0]} {result[1]}")