def minSubArrayLen(target, nums):
    if sum(nums) < target:
        return 0
    if max(nums) > target:
        return 1
    ans = float("inf")
    l = 0
    curr_sum = 0
    for r, val in enumerate(nums):
        curr_sum += val
        while curr_sum >= target:
            ans = min(ans, r - l + 1)
            curr_sum -= nums[l]
            l += 1

    return ans


if __name__ == '__main__':
    n = [2,3,1,2,4,3]
    result = minSubArrayLen(7, n)
    print(result)


