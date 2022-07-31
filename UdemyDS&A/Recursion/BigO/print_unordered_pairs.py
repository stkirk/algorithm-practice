# What is the runtime of the code below?

def print_unordered_pairs(array):
    for i in range(0, len(array)): # O(n)
        for j in range(i+1, len(array)): # 1 + 2 + 3 + (n-3) + (n-2) + (n-1) = n(n-1)/2 = n^2/2 + n
            print(array[i], array[j]) #O(1)

# Time Complexity: 
    # Counting iterations --> O(n) * O(n*(n-1)/2+n) = n^2
    # Average Work --> Outer loop O(n), inner loop n/2 = n^2
