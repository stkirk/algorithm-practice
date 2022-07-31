# What is the runtime of the below code?

def print_pairs(array):
    for i in array: # O(n)
        for j in array: # O(n)
            print(str(i)+',',str(j)) # O(1)

# Time Complexity: O(n^2) quadratic, nested loops each growing linearly with input size
