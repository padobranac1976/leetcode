def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    idx = 0
    while idx < len(arr):
        if arr[idx] != 0:
            idx += 1
            continue

        if idx == len(arr) - 2:
            arr[idx + 1] = 0
        else:
            for j in range(len(arr) - 1, idx + 1, -1):
                arr[j] = arr[j - 1]
            arr[j - 1] = 0
        idx += 2
    print(arr)


if __name__ == '__main__':
    n = [1,0,2,3,0,4,5,0]
    result = duplicateZeros(n)
    print(result)


