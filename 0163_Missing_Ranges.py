def findMissingRanges(nums, lower, upper):
    if lower not in nums:
        nums = [lower - 1] + nums
    if upper not in nums:
        nums.append(upper + 1)
    out = []
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff == 2:
            out.append(str(nums[i] - 1))
        elif diff > 1:
            out.append(f'{nums[i - 1] + 1}->{nums[i] - 1}')

    return out


if __name__ == '__main__':
    n = [0,1,3,50,75]
    l = 0
    u = 99
    print(findMissingRanges(n, l, u))