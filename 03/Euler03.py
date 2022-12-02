def primeFactors(n):
    factors = []
    c = 2
    while(n > 1):
        if(n % c == 0):
            #print(c, end=" ")
            factors.append(c)
            n = n / c
        else:
            c = c + 1
    return factors

num = 600851475143
print(max(primeFactors(num)))
