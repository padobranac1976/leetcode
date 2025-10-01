def longestIncreasingPath(matrix):
    memo = {}

    def dfs(i, j, prev):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and prev < matrix[i][j]:
            if (i, j) in memo: return memo[(i, j)]

            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
            memo[(i, j)] = res
            return res
        return 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dfs(i, j, -1)

    return max(memo.values())




if __name__ == '__main__':
    input1 = [[9,9,4],[6,6,8],[2,1,1]]
    print(longestIncreasingPath(input1))