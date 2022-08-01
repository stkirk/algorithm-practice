# Find the missing number in an array of ints 1 to n

from pkg_resources import find_distributions


nums_lst = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
nums_lst = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19, 11]

def find_missing(nums, n):
    # sum of sequence should be n(n+1)/2
    sequence_sum = n*(n+1)/2
    nums_sum = sum(nums)
    missing = sequence_sum - nums_sum
    return int(missing)

print(find_missing(nums_lst, 20))
