# Convert a number from decimal to binary using recursion

# Recursive Case:
    # Decimal to binary
        # 1- Divide number by 2
        # Get integer quotient for next iteration
        # remainder becomes binary digit
        # repeat until quotient == 0
    # Reverse this process because we need to start at the ones place (which would be last if we just followed these steps in order)
    # f(n) = n % 2 + 10 * f(n//2)

# Base Case:
    # get n all the way down to the ones place
    # when n gets to 0 return 0
    # when n is 1 return 1

# Edge Cases:
    # input is a non integer

def dec_to_bin(n):
    # Base Case:
    if n == 0:
        return 0
    # Recursive Case:
    else:
        return n % 2 + 10 * dec_to_bin(n//2)

print(dec_to_bin(10)) # 1010 
print(dec_to_bin(13)) # 1101
