def peakIndexInMountainArray(arr):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid+1]:
            lo = mid + 1
        else:
            hi = mid
    return lo




if __name__ == '__main__':
    input1 = [24,69,100,99,79,78,67,36,26,19]
    print(peakIndexInMountainArray(input1))