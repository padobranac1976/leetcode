def maxDistToClosest(seats):
    l = 0
    r = seats.index(1)
    maximum = r - l
    if len(seats) == 2:
        return 1
    while r < len(seats):
        if seats[r] == 0:
            maximum = max(maximum, (r - l + 1) // 2)

        else:
            l = r
        r += 1
    if seats[-1] == 0:
        maximum = max(maximum, r - l - 1)
    return maximum


if __name__ == '__main__':
    n = [1,0,0,0]
    print(maxDistToClosest(n))