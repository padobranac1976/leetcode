def sumOddLengthSubarrays(arr):
    length = len(arr)
    ans = 0

    for i in range(length):
        ans += ((i + 1) * (length - i) + 1) // 2 * arr[i]
    return ans;


if __name__ == '__main__':
    n = [1,4,2,5,3]
    result = sumOddLengthSubarrays(n)
    print(result)


