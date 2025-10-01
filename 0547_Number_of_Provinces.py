def findCircleNum(isConnected):
    def dfs(m, visited, i):
        for j in range(len(m)):
            if m[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                dfs(m, visited, j)

    n = len(isConnected)
    visited = [0] * n
    ans = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(isConnected, visited, i)
            ans += 1

    return ans


if __name__ == '__main__':
    n = [[1,1,0],[1,1,0],[0,0,1]]
    result = findCircleNum(n)
    print(result)


