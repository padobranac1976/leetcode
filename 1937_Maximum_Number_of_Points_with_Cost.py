def maxPoints(points):
    for i, row in enumerate(points[:-1]):
        for j in range(1, len(row)):
            row[j] = max(row[j], row[j - 1] - 1)

        for j in range(len(row) - 2, -1, -1):
            row[j] = max(row[j], row[j + 1] - 1)

        for j in range(len(row)):
            points[i + 1][j] += points[i][j]
    return max(points[-1])


if __name__ == '__main__':
    string = [[1,5],[2,3],[4,2]]
    result = maxPoints(string)
    print(result)