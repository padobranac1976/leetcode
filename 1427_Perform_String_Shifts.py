def stringShift(s, shift):
    for d, a in shift:
        a = a % len(s)
        if d == 0:
            s = s[a:] + s[:a]
        else:
            s = s[-a:] + s[:-a:]

    return s


def stringShift2(s, shift):
    final_shift = 0
    for d, a in shift:
        if d == 0:
            final_shift += a
        else:
            final_shift -= a
    final_shift %= len(s)
    return s[final_shift:] + s[:final_shift]


if __name__ == '__main__':
    string = "abcdefg"
    shft = [[1,1],[1,1],[0,2],[1,3]]
    result = stringShift(string, shft)
    result2 = stringShift2(string, shft)
    print(result)
    print(result2)