# given two integers, find the greatest common denominator recursively

# Recursive Case:
    # common_denominator = n % denominator == 0 and m % denominator == 0
    # gcd(8,12) = 4
        # 8 = 2*2*2
        # 12 = 2*2*3
    # Euclidean algorithm:
        # gcd(48,18)
            # 48/18 = 2, remainder 12
            # 18/12 = 1, remainder 6
            # 12/6 = 2, remainder 0
            # assign n,m to big, small
            # gcd(big, small) = gcd(small, big%small)
# Base Case:
    #gcd(a,0) == a
# Edge Cases:
    # a and b are entered at random so a > b or b > a
    # a or b are negative numbers, just convert to positive numbers
    # a or b or both are prime numbers
    # a or b are not ints

def gcd(a,b):
    # Edge cases and constraints
    assert int(a) == a and int(b) == b, 'The numbers a and b must be integers'
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    # Base Case:
    if b == 0:
        return a
    # Recursive Case:
    else:
        return gcd(min(a,b), (max(a, b) % min(a, b)))

print(gcd(48,18)) # 6
print(gcd(18,48)) # 6
print(gcd(-18,-48)) # 6
print(gcd(-18,-4.8)) # 6
