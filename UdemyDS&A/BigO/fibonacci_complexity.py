# What is the runtime of the code below?

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# Time Complexity of recursive function, recursive_branches^depth, depth is n
    # O(2^n)
