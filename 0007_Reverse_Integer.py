def reverse(x: int) -> int:
    list_x = list(str(x))
    sign = 1
    if list_x[0] == '-':
        sign = -1
        list_x = list_x[1:]

    for i in range(len(list_x) // 2):
        head = list_x[i]
        list_x[i] = list_x[-1 - i]
        list_x[-1 - i] = head

    answer = sign * int("".join(list_x))

    if -2 ** 31 <= answer <= 2 ** 31:
        return answer
    else:
        return 0


if __name__ == '__main__':
    x = -123
    result = reverse(x)
    print(result)


