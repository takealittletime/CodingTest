def prime_factorization(n):
    result = []
    # Handle the factor 2 separately to simplify the loop for odd factors
    while n % 2 == 0:
        result.append(2)
        n //= 2

    # Handle odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            result.append(i)
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        result.append(n)

    return result

    

n = int(input().strip())
results = prime_factorization(n)

for result in results:
    print(result)