def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    mp = {}

    l = 0
    for r in range(n):
        if s[r] in mp:
            l = max(mp[s[r]], l)

        ans = max(ans, r - l + 1)
        mp[s[r]] = r + 1

    return ans


if __name__ == '__main__':
    string = "abcabcbb"
    result = lengthOfLongestSubstring(string)
    print(result)


