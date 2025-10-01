def removeDuplicates(nums):
    left = 0

    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            nums[left + 1] = nums[right]
            left += 1

    return nums[:left+1]


if __name__ == '__main__':
    n = [1,1,2]
    result = removeDuplicates(n)
    print(result)


