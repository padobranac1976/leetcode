from collections import Counter


def findAnagrams(s, p):
    if len(s) < len(p):
        return []

    p_count = Counter(p)
    s_count = Counter()

    output = []
    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1

        if p_count == s_count:
            output.append(i - len(p) + 1)

    return output


if __name__ == '__main__':
    string = "abab"
    phrase = "ab"
    result = findAnagrams(string, phrase)
    print(result)


