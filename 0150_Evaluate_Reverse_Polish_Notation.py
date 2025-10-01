def evalRPN(tokens):
    def calc(t, n1, n2):
        if t == "*":
            return n1 * n2
        elif t == "/":
            if n1 * n2 > 0:
                return n1 // n2
            else:
                return -(n1 // -n2)
        elif t == "+":
            return n1 + n2
        else:
            return n1 - n2

    numbers = []
    for e in tokens:
        if e.isnumeric() or (e[0] == "-" and len(e) > 1 and e[1:].isnumeric()):
            numbers.append(int(e))
        else:
            n2 = numbers.pop()
            n1 = numbers.pop()
            numbers.append(calc(e, n1, n2))

    return numbers.pop()


print(evalRPN(["3","11","+","5","-"]))




