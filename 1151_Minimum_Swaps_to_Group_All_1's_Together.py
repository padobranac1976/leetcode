def minSwaps(data):
    ones = sum(data)
    curr_count, max_count = 0, 0
    l = r = 0

    while r < len(data):
        curr_count += data[r]
        r += 1
        if r - l > ones:
            curr_count -= data[l]
            l += 1

        max_count = max(max_count, curr_count)

    return ones - max_count


if __name__ == '__main__':
    n = [1,0,1,0,1]
    result = minSwaps(n)
    print(result)


