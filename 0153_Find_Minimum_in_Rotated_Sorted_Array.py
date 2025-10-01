def findMin(nums):
    start, end = 0, len(nums) - 1
    minimum = nums[start]
    if minimum < nums[end]:
        return minimum
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < minimum:
            minimum = nums[mid]
            end = mid - 1
        else:
            start = mid + 1

    return minimum


if __name__ == '__main__':
    n = [2,1]
    result = findMin(n)
    print(result)


