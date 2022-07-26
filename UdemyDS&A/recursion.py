# When to use recursion:
    # If problem can be divided into similar sub-problems
    # When we are ok with extra time an space overhead
        # Uses O(n) memory --> inefficient memory usage compared to iteration
    # "Design an algorithm to compute the nth..."
    # "Write an algorithm to list the n..."
    # "Implement a method to compute all..."

# Recursion template
def recursiveMethod(originalParameters):
    # exit from infinite loop: base case
    if "exit condition is satisfied":
        return "some value"
    else:
        recursiveMethod("modifiedParameters")

# example of recursive function that counts to n from 0
def print_n_recursively(n):
    # base case stops recursive calling when n gets small enough
    if n < 1:
        print("base case: n is 0")
    else:
        # modify n to get smaller by 1 each time until the last call reached our base case
        print_n_recursively(n-1)
        print("n is now", n)

print_n_recursively(10)

# How to write recursive method in 3 steps:
    # Step 1 - find the Recursive Case, where and how the function is calling itself with modified parameters
    # Step 2 - find the Base Case, stopping conditions
    # Step 3 - Unintentional Case - the constraint

# calculate factorial of n
    # ex. n=4, 4! = 4*3*2*1 = 24
    # n! = n*(n-1)*(n-2)...*2*1
    # recursive case - n! = n*(n-1)!
def factorial(n):
    # Unintentional Case: if condition returns False, AssertionError is raised:
    assert n >= 0 and int(n) == n, "n must be positive integer only!"
    # Base case: stopping condition on n == 1 or 0, only way n could be 0 is if 0 is passed in
    if n == 0 or n == 1:
        # edge case: 0! == 1 and 1! == 1
        return 1
    else:
        # recursive case
        return n*factorial(n-1)

print(factorial(4))
# print(factorial(-1)) # unintentional case, bad argument
# print(factorial(4.1)) # unintentional case, bad argument
