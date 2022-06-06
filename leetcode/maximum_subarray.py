# Given an array of ints, nums:
# find a contiguous subarray containing at least one number which when all indices are added together create the largest possible sum
# return the sum

def max_subarray(nums):
    # init a sum to first index value
    max_sum = nums[0]
    # init a current sum to 0 that represents the contiguous subarray sum
    current_sum = 0

    # loop through num in nums
    for num in nums:
        # get rid of negative leading index in subarray
        if current_sum < 0:
            # reset current sum to 0
            current_sum = 0

        # compute new current sum using new num
        current_sum += num
        # set max sum to bigger value between exisiting max sum and current sum
        max_sum = max(max_sum, current_sum)

    # return the max sum    
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) # subarray--> [4,-1,2,1] | sum == 6
print(max_subarray([1])) # subarray--> [1] | sum == 1
print(max_subarray([5,4,-1,7,8])) # subarray--> [5,4,-1,7,8] | sum == 23
print(max_subarray([-2, -1, -3, -1, -8]))
