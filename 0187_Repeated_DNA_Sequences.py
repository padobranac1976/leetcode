def findRepeatedDnaSequences(s):
    dna_count = {}
    l = 0
    r = 10
    while r <= len(s):
        if s[l:r] in dna_count:
            dna_count[s[l:r]] += 1
        else:
            dna_count[s[l:r]] = 1

        l += 1
        r += 1

    repeats = []
    for dna in dna_count:
        if dna_count[dna] > 1:
            repeats.append(dna)

    return repeats


if __name__ == '__main__':
    string = "AAAAAAAAAAA"
    result = findRepeatedDnaSequences(string)
    print(result)