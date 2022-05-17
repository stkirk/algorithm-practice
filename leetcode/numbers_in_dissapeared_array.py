# Given a list of n intergers, nums, where all the integers are in the range [1, n]
# Return a list of all the integers in the range [1, n] NOT included in nums
# Try for solution in O(n) runtime

# Set comprehension--> newSet = { expression for element in iterable } 

def find_disappeared_numbers(nums):
    # init set for each num in nums, num is key
    num_set = { num for num in nums}
    # init return list
    disapeared_numbers = []

    # loop through range 1, n
    for num in range(1, len(nums) + 1):
        # if num is in the set continue
        if num in num_set:
            continue
        # else add it to return list
        else:
            disapeared_numbers.append(num)

    return disapeared_numbers

print(find_disappeared_numbers([4,3,2,7,8,2,3,1])) # [5,6]
print(find_disappeared_numbers([1,1])) # [2]
