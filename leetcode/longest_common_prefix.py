# Given a list of strings, strs, find the longest common prefix and return it
# if there is no common prefix, return an empty string

def longest_common_prefix(strs):
    # init lcp empty string to return
    lcp = ""

    # loop through strs
        # if first string set to lcp
        # else:
            # compare new string to lcp letter by letter with loop through min of lengths of the two
                # init empty string for new_lcp
                # if lcp[j] != strs[i][j]:
                    # lcp = new_lcp
                # else:
                    # new_lcp += lcp[j]
    return lcp 

print(longest_common_prefix(["flower","flow","flight"])) # "fl"
print(longest_common_prefix(["flower","flow","f"])) # "f"
print(longest_common_prefix(["dog","racecar","car"])) # ""
