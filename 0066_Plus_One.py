def plusOne(digits):
    i = len(digits) - 1
    while i >= 0 and digits[i] == 9:
        digits[i] = 0
        i -= 1
    if i == -1:
        digits = [1] + digits
    else:
        digits[i] += 1

    return digits



if __name__ == '__main__':
    inpt = [9,9,9,9]
    result = plusOne(inpt)
    print(result)



