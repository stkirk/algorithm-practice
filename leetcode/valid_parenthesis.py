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
        if bracket == '(' or bracket == '[' or bracket == '{':
            # add to brackets list
            brackets.append(bracket)
        # else assume its a close bracket
        else:
            # determine current open bracket as last index in brackets
            current_open_bracket = brackets[-1]

            if bracket == ')':
                # edge case if brackets is empty
                if len(brackets) == 0:
                    return False
                elif current_open_bracket == '(':
                    # pop current open bracket
                    brackets.pop()
                # else current bracket is wrong type return False
                else:
                    return False

            elif bracket == ']':
                # edge case if brackets is empty
                if len(brackets) == 0:
                    return False
                elif current_open_bracket == '[':
                    # pop current open bracket
                    brackets.pop()
                # else current bracket is wrong type return False
                else:
                    return False

            # else bracket is '}'
                # edge case if brackets is empty
                if len(brackets) == 0:
                    return False
                elif current_open_bracket == '{':
                    # pop current open bracket
                    brackets.pop()
                # else current bracket is wrong type return False
                else:
                    return False

    # if len of brackets is 0
    if len(brackets) == 0:            
        return True
    else:
        return False

# print(is_valid_brackets("()")) # True
print(is_valid_brackets("()[]{}")) # True
# print(is_valid_brackets("(]")) # False
