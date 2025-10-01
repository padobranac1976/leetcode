def minHeightShelves(books, shelfWidth):
    n = len(books)
    dp = [float("inf")] * n
    dp[0] = books[0][1]  # first book will always on it's own row
    for i in range(1, n):  # for each book
        cur_w, height_max = books[i][0], books[i][1]
        dp[i] = dp[i - 1] + height_max  # initialize result for current book `dp[i]`
        for j in range(i - 1, -1, -1):
            if cur_w + books[j][0] > shelfWidth:
                break
            cur_w += books[j][0]
            height_max = max(height_max, books[j][1])  # update current max height
            dp[i] = min(dp[i], (dp[j - 1] + height_max) if j - 1 >= 0 else height_max)
    return dp[n - 1]


if __name__ == '__main__':
    n = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    result = minHeightShelves(n, 4)
    print(result)


