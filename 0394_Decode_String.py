def decodeString(s):
    numbers = []
    strings = []
    current_string = ""
    decoded_string = ""
    k = 0

    for c in s:
        if c.isnumeric():
            k = k * 10 + ord(c) - ord('0')

        elif c == "[":
            numbers.append(k)
            strings.append(current_string)
            current_string = ""
            k = 0
        elif c == "]":
            decoded_string = strings.pop()
            decoded_string += current_string * numbers.pop()
            current_string = decoded_string

        else:
            current_string += c
    return current_string


if __name__ == '__main__':
    input1 = "3[a]2[bc]"
    print(decodeString(input1))



