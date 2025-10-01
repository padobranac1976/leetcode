def longestConsecutive(nums):
    all_nums = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in all_nums:
            streak = 1
            current = n

            while current + 1 in all_nums:
                streak += 1
                current += 1
            longest = max(longest, streak)

    return longest


if __name__ == '__main__':
    g = [0,3,7,2,5,8,4,6,0,1]
    result = longestConsecutive(g)
    print(result)


