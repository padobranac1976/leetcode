def canConvert(str1, str2):
    if str1 == str2:
        return True

    hash_table = {}
    unique_chars_in_s2 = set()

    for i, c in enumerate(str1):
        if c not in hash_table:
            hash_table[c] = str2[i]
            unique_chars_in_s2.add(str2[i])
        elif hash_table[c] != str2[i]:
            return False

    if len(unique_chars_in_s2) < 26:
        return True

    return False


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "ccdee"
    result = canConvert(s1, s2)
    print(result)



