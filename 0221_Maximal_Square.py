def maximalSquare(matrix):
    ans = 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])

    return ans**2


if __name__ == '__main__':
    inpt = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    result = maximalSquare(inpt)
    print(result)



