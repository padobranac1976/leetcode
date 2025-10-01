def containsNearbyDuplicate(nums, k):
    numbers = {}

    for i, n in enumerate(nums):
        if n in numbers and i - numbers[n] <= k:
            return True

        numbers[n] = i

    return False


if __name__ == '__main__':
    n = [1,2,3,1]
    result = containsNearbyDuplicate(n, 3)
    print(result)


