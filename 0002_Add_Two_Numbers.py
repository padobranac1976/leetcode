def addTwoNumbers(l1, l2):
    length = max(len(l1), len(l2))
    result = []
    carry = 0
    for i in range(length):
        if len(l1) > 0:
            d1 = l1.pop()

        else:
            d1 = 0
        if len(l2) > 0:
            d2 = l2.pop()
        else:
            d2 = 0
        result.append((carry + d1 + d2) % 10)
        carry = (carry + d1 + d2) // 10
    if carry == 1:
        result.append(carry)
    return result


if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    result = addTwoNumbers(l1, l2)
    print(result)


