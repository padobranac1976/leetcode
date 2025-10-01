def maxArea(height):
    l = 0
    r = len(height) - 1
    maxA = 0
    while l < r:
        w = r - l
        h = min(height[l], height[r])
        maxA = max(maxA, w * h)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxA


if __name__ == '__main__':
    h = [1,8,6,2,5,4,8,3,7]
    result = maxArea(h)
    print(result)


