# Given a list of strings, strs, find the longest common prefix and return it
# if there is no common prefix, return an empty string

def longest_common_prefix(strs):
    # init lcp empty string to return
    lcp = ""

    # loop through range of len of first string
        # compare all subsequent strings in strs to strs[0]
        # loop through all str in strs
            # if i is out of range of str or str[i] != strs[0][i]
                # we have an lcp
            # all other scenarios add strs[0][i] to lcp
    
    return lcp 

print(longest_common_prefix(["flower","flow","flight"])) # "fl"
print(longest_common_prefix(["flower","flow","f"])) # "f"
print(longest_common_prefix(["dog","racecar","car"])) # ""
