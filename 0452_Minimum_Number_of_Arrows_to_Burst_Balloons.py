def findMinArrowShots(points):
    points.sort()
    if len(points) == 0:
        return 0

    arrows = 0
    while len(points) > 0:
        start, end = points.pop(0)
        while len(points) > 0 and end >= points[0][0]:
            s, e = points.pop(0)
            end = min(e, end)
        arrows += 1

    return arrows


if __name__ == '__main__':
    n = [[10,16],[2,8],[1,6],[7,12]]
    result = findMinArrowShots(n)
    print(result)


