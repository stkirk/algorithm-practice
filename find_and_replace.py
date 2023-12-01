import fileinput

user_file = input('Drag and drop the text file you want edited: ')
search_param = input('What string would you like to replace? ' )
replacement_param = input('What would you like to replace it with? ')

# user_file coming in with '' already on it so when input convers to a string we end up with something like "'/Users/shanekirk/Desktop/find_and_replace.txt'"
# change this to conditional if ' is present when validating that the file looks correctly formatted
user_file = user_file.replace("'", "")

file_in = fileinput.input(files=user_file)
file_in = open(user_file, "r+")
text = file_in.readlines()
# text = text.replace(search_param, replacement_param)
# file_in.close()
print(text)
