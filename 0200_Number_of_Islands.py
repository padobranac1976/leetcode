def numIslands(grid):
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands += 1
                partOfIsland(i, j, grid)
    return islands


def partOfIsland(i, j, grid):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
        return
    else:
        grid[i][j] = '0'
        partOfIsland(i, j + 1, grid)
        partOfIsland(i, j - 1, grid)
        partOfIsland(i + 1, j, grid)
        partOfIsland(i - 1, j, grid)


if __name__ == '__main__':
    g = [[]]
    result = numIslands(g)
    print(result)


