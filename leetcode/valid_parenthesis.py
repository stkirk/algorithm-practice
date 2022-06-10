# given a string, s, conatining just the chars '(', ')', '{', '}', '[' and ']'
# determine if s is a valid sequence of brackets
# open brackets must be closed by the same type of bracket
# open brackets must be closed in the correct order

def is_valid_brackets(s):
    # init list for each brackets
    brackets = []

    # loop through bracket in s
    for bracket in s:
        # if bracket is an open
        if bracket == '(' or '[' or '{':
            # add to paren list
            brackets.append(bracket)
        # else assume its a close bracket
            # determine current open bracket as last index in brackets
            # if bracket is ')'
                # edge case if brackets is empty
                    # return False
                # elif current bracket is '(':
                    # pop current open bracket
                    # brackets.pop()
                # else current bracket is wrong type return False

            # elif bracket is ']'
                # edge case if brackets is empty
                    # return False
                # elif current bracket is '[':
                    # pop current open bracket
                    # brackets.pop()
                # else current bracket is wrong type return False

            # else bracket is '}'
                # edge case if brackets is empty
                    # return False
                # elif current bracket is '{':
                    # pop current open bracket
                    # brackets.pop()
                # else current bracket is wrong type return False

    # if len of all lists is 0            
    return True
    # else return False

print(is_valid_brackets("()")) # True
print(is_valid_brackets("()[]{}")) # True
print(is_valid_brackets("(]")) # False
