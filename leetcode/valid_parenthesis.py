# given a string, s, conatining just the chars '(', ')', '{', '}', '[' and ']'
# determine if s is a valid sequence of brackets
# open brackets must be closed by the same type of bracket
# open brackets must be closed in the correct order

def is_valid_brackets(s):
    # init deques for each bracket type

    # loop through bracket in s
        # if '('
            # add to paren deque
        # elif '['
            # add to square deque
        # elif '{'
            # add to curly deque
        # elif ')'
            # if len(parens) == 0:
                # return False
            # else:
                # pop a bracket off parens
        # elif ']'
            # if len(squares) == 0:
                # return False
            # else:
                # pop a bracket off squares
        # elif '}'
            # if len(curlies) == 0:
                # return False
            # else:
                # pop a bracket off curlies

    # if len of all deques is 0            
    return True

print(is_valid_brackets("()")) # True
print(is_valid_brackets("()[]{}")) # True
print(is_valid_brackets("(]")) # False
