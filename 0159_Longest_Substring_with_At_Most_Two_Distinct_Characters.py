def lengthOfLongestSubstringTwoDistinct(s):
    l = r = 0
    d = {}
    maximum = 0
    while r < len(s):
        d[s[r]] = r
        r += 1

        if len(d) == 3:
            idx = min(d.values())
            del d[s[idx]]
            l = idx + 1

        maximum = max(maximum, r - l)
    return maximum


if __name__ == '__main__':
    input1 = "ccaabbb"
    print(lengthOfLongestSubstringTwoDistinct(input1))