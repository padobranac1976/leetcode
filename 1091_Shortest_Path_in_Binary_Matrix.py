def shortestPathBinaryMatrix(grid):
    def find_neighbours(f, x, y, g, dist):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for d in directions:
            x_ = x + d[0]
            y_ = y + d[1]
            if 0 <= x_ < len(g) and 0 <= y_ < len(g) and g[x_][y_] == 0:
                frontier.append((x_, y_))
                g[x_][y_] = dist + 1

    if grid[0][0] != 0 or grid[len(grid) - 1][len(grid) - 1] != 0:
        return -1

    frontier = [(0, 0)]
    grid[0][0] = 1

    while len(frontier) > 0:
        i, j = frontier.pop(0)
        distance = grid[i][j]
        if i == j == len(grid) - 1:
            return distance
        find_neighbours(frontier, i, j, grid, distance)

    return -1


if __name__ == '__main__':
    g = [[0,0,0],[1,1,0],[1,1,0]]
    result = shortestPathBinaryMatrix(g)
    print(result)