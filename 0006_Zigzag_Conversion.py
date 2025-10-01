def convert(s, numRows):
    if numRows == 1:
        return s
    output = [""] * min(numRows, len(s))
    curr_row = 0
    down = False

    for c in s:
        output[curr_row] += c
        if curr_row == 0 or curr_row == numRows - 1:
            down = not down
        curr_row += 1 if down else -1

    return "".join(output)


if __name__ == '__main__':
    n = "PAYPALISHIRING"
    result = convert(n, 3)
    print(result)


