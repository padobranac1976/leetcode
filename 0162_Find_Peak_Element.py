def findPeakElement(nums):
    nums = [float("-infinity")] + nums + [float("-infinity")]
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > nums[mid + 1]:
            end = mid - 1
        else:
            start = mid + 1

    return start - 1


if __name__ == '__main__':
    n = [1,2,1,3,5,6,4]
    result = findPeakElement(n)
    print(result)


