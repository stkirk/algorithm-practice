# Given an array of ints, return the product of all elements in the array recursively

def product_of_arr(arr):
    # Base Case: only 1 element in arr
    if len(arr) == 1:
        return arr[0]
    #Recursive Case: f(arr) = arr[0]*fn(arr[1:]) --> slice arr such that first element is gone in next iteration
    else:
        return arr[0] * product_of_arr(arr[1:])

print(product_of_arr([1,2,3,10])) # 60
