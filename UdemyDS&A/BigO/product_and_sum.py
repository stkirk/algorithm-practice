# calculate the runtime of the code below:

def foo(array):
    sum = 0 # O(1)
    product = 1 #O(1)

    for i in array: # O(n)
        sum += 1 # O(1)

    for i in array: # O(n)
        product *= i # O(1)
    
    print("Sum = "+str(sum)+", Product = "+str(product)) # O(1)

# Big O
    # Time Complexity --> O(n)
        # Two loops over the input array would be 2n, plus seperate operations assignments
    # Space Complexity -> O(3) == O(1)
