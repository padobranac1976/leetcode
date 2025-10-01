def subsetsWithDup(nums):
    out = [[]]
    for n in nums:
        temp = []
        for s in out:
            temp2 = list(s)
            temp2.append(n)
            temp2.sort()
            if temp2 not in out:
                temp.append(temp2)
        if temp not in out:
            out += temp[:]

    return out


if __name__ == '__main__':
    string = [1,2,2]
    result = subsetsWithDup(string)
    print(result)