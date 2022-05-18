# Given a non-empty list of ints, nums, every int appears twice except for one. 
# Return that single non-repeated int
# Solution must be O(n) Time complexity and O(1) Space complexity

import enum


def single_number(nums):
    # create dictionary, key is num value is occurences
    num_occurence = {}
    for num in nums:
        if num not in num_occurence:
            num_occurence[num] = 1
        else:
            num_occurence[num] += 1

    # loop through each num in nums
    for num in nums:
        # if dict[num] == 1
        if num_occurence[num] == 1:
            return num
    return -1

# print(single_number([2,2,1])) # 1
# print(single_number([4,1,2,1,2])) # 4
# print(single_number([1])) # 1

def single_number_constant_space(nums):
    # safety check for single item in nums
    if len(nums) == 1:
        return nums[0]
    # order nums in place
    nums.sort()
    # loop through each i, num in enumerate nums
    for i, num in enumerate(nums):
        if i == 0 and num != nums[i + 1]:
            return num
        elif i == (len(nums) - 1):
            return num
        elif nums[i] != nums[i - 1]:
            if nums[i] != nums[i + 1]:
                return num
        elif nums[i] != nums[i + 1]:
            if nums[i] != nums[i - 1]:
                return num
        else:
            continue
    
    return nums

print(single_number_constant_space([2,2,1])) # 1
print(single_number_constant_space([4,1,2,1,2])) # 4
print(single_number_constant_space([1])) # 1
