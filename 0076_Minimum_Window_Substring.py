def minWindow(s, t):
    if not t or not s or len(t) > len(s):
        return ""

    letters = {}
    for l in t:
        letters[l] = letters.get(l, 0) + 1

    required = len(letters)

    lo = hi = 0
    current_window = {}
    formed = 0
    ans = (float("inf"), None, None)
    while hi < len(s):
        c = s[hi]
        current_window[c] = current_window.get(c, 0) + 1
        if c in letters and current_window[c] == letters[c]:
            formed += 1

        while lo <= hi and formed == required:
            c = s[lo]
            if hi - lo + 1 < ans[0]:
                ans = (hi - lo + 1, lo, hi)

            current_window[c] -= 1
            if c in letters and current_window[c] < letters[c]:
                formed -= 1

            lo += 1
        hi += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


if __name__ == '__main__':
    source = "ADOBECODEBANC"
    target = "ABC"
    result = minWindow(source, target)
    print(result)



