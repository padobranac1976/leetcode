def findDuplicates(nums):
    out = []
    for n in nums:
        if nums[abs(n) - 1] > 0:
            nums[abs(n) - 1] = -nums[abs(n) - 1]
        else:
            out.append(abs(n))
    return out


if __name__ == '__main__':
    n = [2,2]
    result = findDuplicates(n)
    print(result)


