# Given an array, nums, containing n distinct integers in the range 0 to n
# return the only number missing from the array
# ex. if len(nums) is 2, n == 2, the range is 0, 1, 2

def missing_number(nums):
    # sort nums
    in_order = sorted(nums)
    # loop over range(len(nums) + 1)
    for i in range(len(nums) + 1):
        # safety check to not go out of range of nums
        if i == (len(nums)):
            return i
        # if i, the range index for loop, == nums[i] continues
        elif i == in_order[i]:
            continue
        # else return i because it is missing from nums 
        return i
    return -1

print(missing_number([3,0,1])) # 2
print(missing_number([0,1])) # 2
print(missing_number([9,6,4,2,3,5,7,0,1])) # 8
