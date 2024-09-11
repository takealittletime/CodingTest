def mod_exp(A,B,C):
    if B == 0:
        return 1
    
    half = mod_exp(A, B//2, C)
    
    if B % 2 == 0:
        return (half * half) % C
    
    else:
        return (half * half * A) % C

A, B, C = map(int, input().split())

print(mod_exp(A, B, C))