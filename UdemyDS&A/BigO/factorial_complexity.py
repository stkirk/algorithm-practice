# What is the runtime of the code below?

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

# n! = 1*2*3...*n
# Time Complexity: O(n), as n gets bigger operations are added linearly
