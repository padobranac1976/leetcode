def longestPalindrome(s):
    letters = {}
    longest = 0
    for l in s:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1

    odd = 0
    for ch in letters:
        if letters[ch] % 2 == 0:
            longest += letters[ch]
        else:
            if not odd:
                odd += 1
            longest += letters[ch] // 2 * 2

    return longest + odd


if __name__ == '__main__':
    string = "abccccdd"
    result = longestPalindrome(string)
    print(result)