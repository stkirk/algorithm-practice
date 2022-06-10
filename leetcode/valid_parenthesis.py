# given a string, s, conatining just the chars '(', ')', '{', '}', '[' and ']'
# determine if s is a valid sequence of brackets
# open brackets must be closed by the same type of bracket
# open brackets must be closed in the correct order

def is_valid_brackets(s):
    return True

print(is_valid_brackets("()")) # True
print(is_valid_brackets("()[]{}")) # True
print(is_valid_brackets("(]")) # False
