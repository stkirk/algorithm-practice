# Given a string, s, and a list of strings, wordDict:
# return True if s can be made from the words in wordDict
# return False if it can't
# the same word from wordDict can be used multiple times

def word_break(s, wordDict):
    word_model = [False] * (len(s) + 1)
    word_model[len(s)] = True

    for idx in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if (idx + len(word) <= len(s) and s[idx : idx + len(word)] == word):
                word_model[idx] = word_model[idx + len(word)]
            if word_model[idx]:
                break

    return word_model[0]

print(word_break("leetcode", ["leet","code"])) # True
print(word_break("applepenapple",["apple","pen"])) # True
print(word_break("catsandog",["cats","dog","sand","and","cat"])) # False
print(word_break("rrcc",["rc"])) # False
