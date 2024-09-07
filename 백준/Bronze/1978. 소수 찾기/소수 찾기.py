def checkPrime (n):
    if n <= 1:
        return False
    
    elif n == 2:
        return True
    
    else:
        for i in range (2,n):
            if n%i == 0:
                return False
        return True

N = int(input().strip())

count = 0

nums = list(map(int,input().strip().split()))


for num in nums:
    if checkPrime(num):
        count += 1

print(count)
