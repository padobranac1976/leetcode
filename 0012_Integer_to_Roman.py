def intToRoman(num):
    integer = list(str(num)[::-1])
    factor = 1
    roman = ""
    while integer:
        digit = int(integer.pop(0))
        if digit <= 3:
            if factor == 1:
                roman += "I" * digit
            elif factor == 10:
                roman += "X" * digit
            elif factor == 100:
                roman += "C" * digit
            elif factor == 1000:
                roman += "M" * digit
        elif digit == 4:
            if factor == 1:
                roman += "VI"
            elif factor == 10:
                roman += "LX"
            elif factor == 100:
                roman += "DC"
        elif digit == 5:
            if factor == 1:
                roman += "V"
            elif factor == 10:
                roman += "L"
            elif factor == 100:
                roman += "D"
        elif digit <= 8:
            if factor == 1:
                roman += "I" * (digit - 5) + "V"
            elif factor == 10:
                roman += "X" * (digit - 5) + "L"
            elif factor == 100:
                roman += "C" * (digit - 5) + "D"
        elif digit == 9:
            if factor == 1:
                roman += "XI"
            elif factor == 10:
                roman += "CX"
            elif factor == 100:
                roman += "MC"
        factor *= 10

    return roman[::-1]


if __name__ == '__main__':
    n = 58
    result = intToRoman(n)
    print(result)


