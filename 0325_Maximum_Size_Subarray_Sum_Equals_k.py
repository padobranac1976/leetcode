def maxSubArrayLen(nums, k):
    prefix_sum = longest_sub = 0
    indices = dict()

    for i, val in enumerate(nums):
        prefix_sum += val

        if prefix_sum == k:
            longest_sub = i + 1

        if prefix_sum - k in indices:
            longest_sub = max(longest_sub, i - indices[prefix_sum - k])

        if prefix_sum not in indices:
            indices[prefix_sum] = i

    return longest_sub


if __name__ == '__main__':
    n = [-2,-1,2,1]
    result = maxSubArrayLen(n, 1)
    print(result)


