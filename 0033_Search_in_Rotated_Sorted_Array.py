def search(n, t):
    start, end = 0, len(n) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if n[mid] == t:
            return mid
        elif n[mid] >= n[start]:
            if n[mid] > t >= n[start]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if n[mid] < t <= n[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == '__main__':
    nums = [5,1,2,3,4]
    target = 1
    result = search(nums, target)
    print(result)


