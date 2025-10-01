def multiply(num1, num2):
    ans = []
    carry = 0
    for i, d1 in enumerate(n1[::-1]):
        out = ""
        for d2 in n2[::-1]:
            mul = str(int(d1) * int(d2) + carry)
            out += mul[-1]

            if len(mul) > 1:
                carry = int(mul[:-1])
            else:
                carry = 0
        if carry > 0:
            out += str(carry)
            carry = 0
        ans.append(out[::-1]+"0"*i)
    return str(sum(map(int, ans)))


if __name__ == '__main__':
    n1 = "123"
    n2 = "456"
    result = multiply(n1, n2)
    print(result)