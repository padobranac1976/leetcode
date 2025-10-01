def floodFill(image, sr, sc, newColor):
    def dfs(m, x, y, colour, target):
        if x < 0 or x == len(m) or y < 0 or y == len(m[0]) or m[x][y] != colour:
            return
        m[x][y] = target
        dfs(m, x + 1, y, colour, target)
        dfs(m, x - 1, y, colour, target)
        dfs(m, x, y + 1, colour, target)
        dfs(m, x, y - 1, colour, target)

    dfs(image, sr, sc, image[sr][sc], newColor)
    return image


if __name__ == '__main__':
    n = [[1,1,1],[1,1,0],[1,0,1]]
    result = floodFill(n, 1, 1, 2)
    print(result)


