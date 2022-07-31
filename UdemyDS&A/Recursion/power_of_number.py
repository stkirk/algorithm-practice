# Given the base number and exponent
# Calculate the power of a number using recursion
# x^n = x*x*x...(n times)
# 2^4 = 2*2*2*2

# Recursive Case: x^a * x^b = x^a+b
    # x^3 * x^4 = x^3+4
    # x^n = x * x^n-1
# Base Case:
    # when exp gets down to 0 return 1, n^0 == 1
# Edge Cases - the constraints
    # power(-1,2)
    # power(3.2,2)
    # power(2,1.2) --> problem
    # power(2,-1) --> problem

def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'The exponent must be a positive integer'
    # Base Case:
    if exp == 0:
        return 1
    else:
        # Recursive Case:
        return base * power(base, exp-1)

print(power(2,4)) # 16
print(power(2,1)) # 2
print(power(-1,2)) # 1
print(power(3.2,2)) # 10.24000
print(power(2,1.2)) # Error
print(power(2, -1)) # Error
