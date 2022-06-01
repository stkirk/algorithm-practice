# Given an array of intergers, nums and an integer, target
# return a list containing the indicies of the two ints in nums that add up to the target
# only 1 solution, can't reuse an integer
# return answer in any order

import enum


def two_sum(nums, target):
    # init dict with complement to num as key, index of num as value
    complements = {(target - num) : i for i, num in enumerate(nums)}
    # loop through nums
        # check if num is in dict
            # if it is, make sure indicies aren't same (no reuse)
            # not reused, return index of num and index of complement
    return complements

print(two_sum([2,7,11,15], 9)) # [0,1]
print(two_sum([3,2,4], 6)) # [1,2]
print(two_sum([3,3], 6)) # [0,1]
