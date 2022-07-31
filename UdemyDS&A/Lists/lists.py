# Lists hold ordered collections of comma-seperated items in square brackets

shopping = ['milk', 'cheese', 'butter']
# find out if element exists in list or not with 'in' operator
print('milk' in shopping)
print('bread' in shopping)
print(23 in shopping)

# Update element in list
intlist = [1,2,3,4,5,6,7]
intlist[2] = 33 # overwrite 3rd element to 33

# Insert at any given location
intlist.insert(0, -1) # inserts new element -1 at beginning of list
print(intlist)
intlist.insert(len(intlist)//2, 333) # inserts 333 in middle of list
print(intlist)
newlist = [888,999]
combined_list = intlist + newlist
print(combined_list)

num_list = [1,2,3,4,5,6,7,8,9,10,11]
# Slice list[start(inclusive):stop(exclusive):step_size]
print(num_list[0:2])
print(num_list[-1]) # last element
# Update multiple elements
num_list[0:2] = ['a', 'b'] # changes first two elements to a,b
print(num_list)

# Removing Elements
last_element = num_list.pop()
print(last_element, num_list)
# specify an element to pop
second_element = num_list.pop(1) # pops second element
print(second_element, num_list)

# Deleting elements
del num_list[1] # deletes 2nd element
print(num_list) 
del num_list[2:4] # deletes 2nd and 3rd elements
print(num_list)

# Remove
num_list.remove(8) # removes an element without knowing the index
print(num_list)

# Searching for an element
nums = [10,20,30,40,50,60,70,80,90]
if 20 in nums:
    print(nums.index(20)) # O(n) --> checks each index one by one
else:
    print('This value does not exist in the list')

# Also search using for loop
