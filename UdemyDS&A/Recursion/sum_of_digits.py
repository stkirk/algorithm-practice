# Find the sum of digits of a positive integer using recursion

# Step 1 - Find the recursive case
    # example: 10, 1 + 0 = 0
    # 10//10 = 1, remainder 0
    # 54//10 = 5, remainder 4
    # 112//10 = 11. remainder 2
        # 11//10 = 1, remainder 1
    # 4//10 = 0, remainder 4
    # our recursive case function: f(n) = n % 10 + f(n // 10)
        # reads: add the remainder of n divided by 10 plus the function result where n/10

def sum_of_digits(n):
    # Base Case:
    if n == 0:
        return 0
    # Recursive Case:
    else:
        return int( n % 10) + sum_of_digits( n // 10)

print(sum_of_digits(4))
print(sum_of_digits(11))
print(sum_of_digits(112))
print(sum_of_digits(10))
