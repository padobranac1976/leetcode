def longestPalindrome(s):
    if len(s) < 1: return ""
    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        length = max(len1, len2)

        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2

    return s[start:end + 1]


def expandAroundCenter(string, left, right):
    l = left
    r = right

    while l >= 0 and r < len(string) and string[l] == string[r]:
        l -= 1
        r += 1
    return r - l - 1


if __name__ == '__main__':
    strng = "babad"
    result = longestPalindrome(strng)
    print(result)