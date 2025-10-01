def longestStrChain(words):
    def dfs(word_dict, word_set, curr_word):
        if curr_word in word_dict:
            return word_dict[curr_word]

        max_len = 1

        for i in range(len(curr_word)):
            new_word = curr_word[:i] + curr_word[i + 1:]
            if new_word in word_set:
                curr_len = 1 + dfs(word_dict, word_set, new_word)
                max_len = max(max_len, curr_len)
        word_dict[curr_word] = max_len
        return max_len

    word_set = set()
    for w in words:
        if w not in word_set:
            word_set.add(w)

    longest_chain = 0
    word_dict = {}
    for w in words:
        longest_chain = max(longest_chain, dfs(word_dict, word_set, w))

    return longest_chain


if __name__ == '__main__':
    strng =  ["a","b","ba","bca","bda","bdca"]
    result = longestStrChain(strng)
    print(result)