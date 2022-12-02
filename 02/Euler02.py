# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8 etc
# Sum = two previous values in the sequence
def fib(n):
    if n in {0, 1}: return n
    else: return fib(n-1)+fib(n-2)

# Function to calculate sum of x amount of fib-numbers
# Modes: Even numbers, Odd numbers or All
def calcFibTotal(maxFib,mode):
    n = 0
    tot = 0
    if mode == 'even':
        while fib(n) <= maxFib:
            if fib(n) % 2 == 0:
                tot += fib(n)
            n += 1
    elif mode == 'odd':
        while fib(n) <= maxFib:
            if fib(n) % 2 != 0:
                tot += fib(n)
            n += 1
    else:
        while fib(n) <= maxFib:
            tot += fib(n)
            n += 1
    return tot

# Answer
print(calcFibTotal(4e6,'even'))

#  Todo: Optimize code for more speedy execution