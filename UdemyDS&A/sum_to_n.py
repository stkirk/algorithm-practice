# Write a recursive function that given an input of n, sums up all non-negative integers up to n

# Step 1 - What is the simpleist possible input?
    # Often the base case
    # n=0 => sum(0) = 0
# Step 2 - play around with examples and visualize
    # what does n=2 look like, n=3...
# Step 3 - relate hard cases to simpler cases
    # if given sum(4), could I solve sum(5)?
        # if we know answer for n=4 all we need to do is add 5 to it to get n=5 case
# Step 4 - Generalize the pattern
    # what is the sum for n = k?
        # just as with with n=5, sum(5) = sum(4) + 5
        # sum(k) = sum(k-1) + k
# Step 5 - Write solutions by combining generalized recursive pattern with the base case:

def sum(n):
    # Base Case:
    if n == 0:
        return 0
    # Recursive Case:
    else:
        return sum(n-1) + n

print(sum(5))

# Recursive Leap of Faith:
    # Assume the simpler cases will work out
