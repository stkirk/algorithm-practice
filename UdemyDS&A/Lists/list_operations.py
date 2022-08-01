# List Operations and built-in functions

a = [1,2,3,4,5,6]
b = [4,5,6,7,8,9]

# Concatenate two lists
c = a + b 
print(c)

# Repeat x times
aaa = a * 3
print(aaa)

# sum all items in list
# sum = sum(a)
# print(sum)
# average of the values in the list
print(sum(a)/len(a))

# String and lists
word = 'spam'
list_from_word = list(word)
print(list_from_word)

sentence = "spam is my favorite food"
word_list_from_sentence = sentence.split()
print(word_list_from_sentence)

# convert back to string
back_to_string = ' '.join(word_list_from_sentence)
print(back_to_string)
