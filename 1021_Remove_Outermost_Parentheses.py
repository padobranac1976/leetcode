def removeOuterParentheses(s):
    stack = []
    output = ""

    for c in s:
        if c == "(":
            if stack:
                output += c
            stack.append(c)
        else:
            stack.pop()
            if stack:
                output += c

    return output


if __name__ == '__main__':
    input1 = "(()())(())(()(()))"
    print(removeOuterParentheses(input1))