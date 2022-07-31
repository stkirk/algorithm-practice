from functools import reduce
# Handy python tricks

# SWAP TWO VARIABLE VALUES
a = 1
b = 2
print(a,b) # 1,2
a,b = b,a
print(a,b) # 2,1

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Map
def square(n):
    return n ** 2
# Map --> applies a function to each item in an iterable and returns a new map object that can be turned into a list. Can pass in existing function or lambda
# squares = list(map(square, numbers))
squares = list(map(lambda num: num**2, numbers))
print(squares)

# Filter --> filter out items in iterable, passing in a boolean function as the first argument
evens = list(filter(lambda num: num%2 == 0, numbers)) # num must pass the boolean test to not be filtered out
print(evens)

# Reduce --> reduce(function, sequence[, initial]) -> value
# applies a function of two arguments cumulatively to the items in a sequence from left to right to reduce the sequence to a single value, if initial is present as 3rd argument it is placed before the sequence and serves as a default if the sequence is empty
product = reduce(lambda x,y: x*y, numbers)
print(product)

# remove duplicate values from a list
duplicates = [1,2,3,4,5,1,1,1,2,3,4,5,5,5]
no_dupes = list(set(duplicates))
print(no_dupes)

# count numbers of occurences of an item in iterable
print(duplicates.count(1)) # number 1 appears 4 times

# which number appears the most times in a list --> returns first occurence if theres a tie
most_repeated = max(set(duplicates), key=duplicates.count)
print(most_repeated)

# Pass in any amount of parameters to a function
def multiple_params(*numbers):
    res = 0
    for num in numbers:
        res += num
    return res
print(multiple_params(5,4,7,987,45,22))

# Reverse a string with slicing
reverse_name = 'Shane'[::-1]
print(reverse_name)

# check for PALINDROME
word = 'racecar'
is_palindrome = word.find(word[::-1])==0
print('is word a palindrome?', is_palindrome)
print('is name a palindrome?', reverse_name.find(reverse_name[::-1])==0) # finds the lowest index of a substring, if the string is a palindrome it follows that the substring will start at index 0

# Unpacking --> assign multiple variables to items in iterables all at once
lst = [1,2,3]
one, two, three = lst
print(one,two,three)

dic = {'a':1, 'b': 2}
# assign KEYS
a, b = dic
print(a,b)
# assign values
a, b = dic.values()
print(a,b)
# assign key, value pairs to a tuple
a,b = dic.items()
print(a,b)
# get all dictionary key:value pairs into a list of tuples (key, value)
print(list(dic.items()))

# Two dimensional array comprehension
two_dimension_arr = [[0 for _ in range(5)] for _ in range(5)] # 5X5 two dimensional array
print(two_dimension_arr)

# Dictionary comprehension, count occurences of something in an iterable
sentence = 'hello my name is tim'
char_count = {char: sentence.count(char) for char in set(sentence)} # turning into a set makes a little more efficient since you are only going through the unique chars and not duplicating work, i.e. counting that there are 3 'm''s 3 times and overwriting each time
print(char_count)

# multiple an object
# say we need a list with the same item the length of an input iterable, this case chars in a sentence
input_list = [[0,1,2]] * len(sentence)
print('multiplied list', input_list)

# Inline ternary
x = 1 if 2 > 3 else 0
print('ternary', x)

# ZIP together iterables
names = ['tim', 'shane', 'billy']
ages = [21, 34, 24]
passing = [True, True, False]
# combine all three lists together into a list of tuples with corresponding(names[i], ages[i], passing[i])
# number of resulting tuples will be min length of all the iterables entered
combined = list(zip(names, ages, passing))
print(combined)

# useful for iterating through multiple lists at the same time
for name, age in zip(names, ages):
    if age < 30:
        print(name)

# Sort by key
lst = [[1,2], [3,4], [4,2], [-1,3], [4,5], [2,3]]
lst.sort() # sorts by first element inside the nested list in ascending order, min value first
lst.sort(reverse=True) # same but in descending order, max value first
lst.sort(key=lambda el: el[1]) # sorts by the second item in each list element
lst.sort(key=lambda el: el[0] + el[1]) # sorts by cumulative total of the two elements
print('sorted list', lst)

# Itertools --> allows to iterate through multiple lists and perform operations on them without creating more lists and no extra memory overhead
# Useful when Space complexity is a constraint
import itertools
lst = [1,2,3,4,5]
sum_list = itertools.accumulate(lst) # this is actually just an iterator, could be used to loop through without converting to a list
print(list(sum_list))

lst2 = ['a', 'b', 'c', 'd']
chain_list = itertools.chain(lst, lst2) # combines the two lists together without creating a third list
for el in chain_list:
    print(el)

names = ['tim', 'shane', 'billy']
passing = [True, True, False]

compressed_lst = itertools.compress(names, passing)
for name in compressed_lst:
    print(name, 'is passing')
