# Fibonacci is a sequence of numbers in which each number is the sum of the two preceding ones starting at 0 and 1
# 0,1,1,2,3,5,8,13,21,34.....

# calculate the nth Fibonacci number in the sequence, Fibonacci(0) == 0
# each Fibonacci number in the sequence is the sum of the two preceding Fibonacci numbers
    # Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)

def fibonacci(n):
    # unintentional case: negative ints and non ints
    assert n >= 0 and int(n) == n, "n must be positive integer only!"
    # base case
    if n == 0 or n == 1:
        return n
    # recursive case: the flow
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
