def isPalindrome(x: int) -> int:
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    x = 121
    result = isPalindrome(x)
    print(result)


