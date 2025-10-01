def backspaceCompare(s, t):
    s_out = []
    for c in s:
        if c == "#":
            if len(s_out) > 0:
                s_out.pop()
        else:
            s_out.append(c)
    t_out = []
    for c in t:
        if c == "#":
            if len(t_out) > 0:
                t_out.pop()
        else:
            t_out.append(c)
    return s_out == t_out


if __name__ == '__main__':
    s1 = "ab#c"
    t1 = "ad#c"
    result = backspaceCompare(s1, t1)
    print(result)


