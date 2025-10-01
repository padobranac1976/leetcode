def totalFruit(fruits):

    n = len(fruits)
    i = j = 0
    freq = dict()
    ans = 0

    while j < n:
        if fruits[j] in freq:
            freq[fruits[j]] += 1
        else:
            freq[fruits[j]] = 1

        if len(freq) <= 2:
            ans = max(ans, j - i + 1)
        else:
            while len(freq) > 2:
                freq[fruits[i]] -= 1
                if freq[fruits[i]] == 0:
                    del freq[fruits[i]]
                i = i + 1

        j = j + 1
        # print(ans)

    return ans


if __name__ == '__main__':
    s = [1,0,1,4,1,4,1,2,3]
    result = totalFruit(s)
    print(result)


