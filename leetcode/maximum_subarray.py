# Given an array of ints, nums:
# find a contiguous subarray containing at least one number which when all indices are added together create the largest possible sum
# return the sum

def max_subarray(nums):
    return -1

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) # subarray--> [4,-1,2,1] | sum == 6
print(max_subarray([1])) # subarray--> [1] | sum == 1
print(max_subarray([5,4,-1,7,8])) # subarray--> [5,4,-1,7,8] | sum == 23
