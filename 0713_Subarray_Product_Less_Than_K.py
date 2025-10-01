def numSubarrayProductLessThanK(nums, k):
    if len(nums) < 2:
        return len(nums)
    if k == 0: return 0

    l = 0
    ans = 0
    prod = 1

    for r, val in enumerate(nums):
        prod *= val
        while prod >= k and l <= r:
            prod /= nums[l]
            l += 1
        ans += r - l + 1
    return ans


if __name__ == '__main__':
    n = [10,5,2,6]
    result = numSubarrayProductLessThanK(n, 100)
    print(result)


