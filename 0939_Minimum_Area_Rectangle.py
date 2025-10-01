def minAreaRect(points):
    if len(points) < 4:
        return 0
    points.sort()
    p = {}
    min_area = float("inf")

    for i in range(1, len(points)):
        curr_x, curr_y = points[i]
        for j in range(i - 1, -1, -1):
            prev_x, prev_y = points[j]

            if prev_x == curr_x:
                key = (prev_y, curr_y)
                if key in p:
                    curr_area = (curr_x - p[key]) * (curr_y - prev_y)
                    min_area = min(curr_area, min_area)

                p[key] = curr_x
            else:
                break
    if min_area == float("inf"):
        return 0
    return min_area


if __name__ == '__main__':
    inpt = [[1,1],[1,3],[3,1],[3,3],[2,2]]
    result = minAreaRect(inpt)
    print(result)



