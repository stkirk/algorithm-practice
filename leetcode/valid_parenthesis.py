# given a string, s, conatining just the chars '(', ')', '{', '}', '[' and ']'
# determine if s is a valid sequence of brackets
# open brackets must be closed by the same type of bracket
# open brackets must be closed in the correct order

def is_valid_brackets(s):
    # init list for brackets
    brackets = []

    # loop through bracket in s
    for bracket in s:
        # if bracket is an open
        if bracket == '(' or bracket == '[' or bracket == '{':
            # add to brackets list
            brackets.append(bracket)
        # else assume its a close bracket
        else:
            # edge case if brackets is empty
            if len(brackets) == 0:
                    return False
            # determine current open bracket as last index in brackets
            current_open_bracket = brackets[-1]

            if bracket == ')':
                if current_open_bracket == '(':
                    # pop current open bracket
                    brackets.pop()
                # else current bracket is wrong type return False
                else:
                    return False

            elif bracket == ']':
                if current_open_bracket == '[':
                    # pop current open bracket
                    brackets.pop()
                # else current bracket is wrong type return False
                else:
                    return False
            # else bracket is '}'
            else:
                if current_open_bracket == '{':
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
# print(is_valid_brackets("()[]{}")) # True
# print(is_valid_brackets("(]")) # False
# print(is_valid_brackets("()({)}")) # False
# print(is_valid_brackets(")(")) # False

# Optimized solution with hashmap
def is_valid_parenthesis_opt(s):
    stack = []
    map_close_to_open = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for bracket in s:
        # if its a close bracket
        if bracket in map_close_to_open:
            # if the stack has something in it and the last item maps to the close bracket
            if stack and stack[-1] == map_close_to_open[bracket]:
                # remove open bracket from stack
                stack.pop()
            else:
                return False
        # else its an open bracket        
        else:
            # add it to the stack
            stack.append(bracket)

    # if stack is empty, syntax is valid
    if not stack:
        return True
    else:
        return False

print(is_valid_parenthesis_opt("()")) # True
print(is_valid_parenthesis_opt("()[]{}")) # True
print(is_valid_parenthesis_opt("(]")) # False
print(is_valid_parenthesis_opt("()({)}")) # False
print(is_valid_parenthesis_opt(")(")) # False
