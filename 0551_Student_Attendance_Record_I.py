def checkRecord(s):
    if s.count("A") >= 2: return False
    if s.count("LLL") > 0: return False
    return True


if __name__ == '__main__':
    input1 = "PPALLP"
    print(checkRecord(input1))