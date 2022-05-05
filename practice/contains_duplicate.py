# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    # init duplicate_tracker dictionary
    duplicate_tracker = {}
    # loop through nums
    for num in nums:
        # if num is in duplicate_tracker dictionary
        if num in duplicate_tracker:
            # number is already in the dictionary, return false
            return True
        else:
            # add num as key, value of 1
            duplicate_tracker[num] = 1
    # loop finished, no duplicates
    return False

# test cases
print(contains_duplicate([1,2,3,1])) # True
print(contains_duplicate([1,2,3,4])) # False
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
