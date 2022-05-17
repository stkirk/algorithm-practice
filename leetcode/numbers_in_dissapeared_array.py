# Given a list of n intergers, nums, where all the integers are in the range [1, n]
# Return a list of all the integers in the range [1, n] NOT included in nums
# Try for solution in O(n) runtime

# Set comprehension--> newSet = { expression for element in iterable } 

def find_disappeared_numbers(nums):
    # init set for each num in nums, num is key
    
    # init return list

    # loop through range 1, n
        # if num is in the set continue
        # else add it to return list

    return [1]

print(find_disappeared_numbers([4,3,2,7,8,2,3,1])) # [5,6]
print(find_disappeared_numbers([1,1])) # [2]
