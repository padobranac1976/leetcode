def removeDuplicates(nums):
    if len(nums) > 2:
        return nums

    left = 0

    for right in range(2, len(nums)):
        if nums[left] != nums[right]:
            nums[left + 2] = nums[right]
            left += 1
    return nums[:left+2]


if __name__ == '__main__':
    n = [1,1,2]
    result = removeDuplicates(n)
    print(result)


