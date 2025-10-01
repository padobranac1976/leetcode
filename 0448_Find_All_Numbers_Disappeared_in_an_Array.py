def findDisappearedNumbers(nums):
    maximum = len(nums)
    ans = []
    all_nums = [0] * maximum

    for n in nums:
        all_nums[n - 1] += 1

    for i, number in enumerate(all_nums):
        if number == 0:
            ans.append(i + 1)

    return ans


if __name__ == '__main__':
    g = [4,3,2,7,8,2,3,1]
    result = findDisappearedNumbers(g)
    print(result)


