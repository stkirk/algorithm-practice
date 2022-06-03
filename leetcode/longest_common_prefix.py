# Given a list of strings, strs, find the longest common prefix and return it
# if there is no common prefix, return an empty string

def longest_common_prefix(strs):
    # init lcp empty string to return

    # can just compare first two strings to get lcp
    # init str1 = strs[0]
    # init str2 = strs[1]

    # loop through range min of lengths of str1 and str2
        # if str1[i] == str2[i]:
            # lcp += str1[i]
        # else:
            # return lcp
    return "strs"

print(longest_common_prefix(["flower","flow","flight"])) # "fl"
print(longest_common_prefix(["dog","racecar","car"])) # ""
