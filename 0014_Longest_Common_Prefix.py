def longestCommonPrefix(strs):
    if len(strs) == 0 or len(strs[0]) == 0:
        return ""
    i = 0
    min_len = float("inf")
    for j, s in enumerate(strs):
        if len(s) < min_len:
            min_len = len(s)
            prefix = strs[j]

    stop = False
    while True:
        for string in strs:
            if i == len(prefix) or string[i] != prefix[i]:
                stop = True
                break

        if stop:
            break
        i += 1
    return prefix[:i]


if __name__ == '__main__':
    n = ["aaa","aa","aaa"]
    result = longestCommonPrefix(n)
    print(result)


