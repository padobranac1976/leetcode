def isValid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    bracket_stack = []
    for i, bracket in enumerate(s):
        if bracket in pairs:
            if bracket_stack:
                opened = bracket_stack.pop()
            else:
                return False

            if pairs[bracket] != opened:
                return False
        else:
            bracket_stack.append(bracket)

    return not bracket_stack


if __name__ == '__main__':
    inpt = "()[]{}"
    result = isValid(inpt)
    print(result)



