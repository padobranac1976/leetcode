def licenseKeyFormatting(s, k):
    s_list = s.upper().replace("-", "")
    if len(s_list) <= k:
        return s_list

    rem = len(s_list) % k
    answer = []
    if rem > 0:
        answer.append(s_list[:rem])
        s_list = s_list[rem:]
    for i in range(0, len(s_list) - k, k):
        word = s_list[i: i + k]
        answer.append(word)
    if len(s_list) <= k:
        answer.append(s_list)
    else:
        answer.append(s_list[i + k:])
    return "-".join(answer)


if __name__ == '__main__':
    l1 = "2-4A0r7-4k"
    l2 = 4
    result = licenseKeyFormatting(l1, l2)
    print(result)


