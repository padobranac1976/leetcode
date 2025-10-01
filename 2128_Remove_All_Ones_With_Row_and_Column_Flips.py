def removeOnes(grid):
    if len(grid) == 1:
        return True
    grid_idx = []

    for idx, row in enumerate(grid):
        inverted_row = []
        for e in row:
            inverted_row.append(0 if e == 1 else 1)
        if inverted_row in grid and idx not in grid_idx:
            i = grid.index(inverted_row)
            grid[i] = row
            grid_idx.append(idx)

    for i in range(len(grid) - 1):
        if grid[i] != grid[i + 1]:
            return False

    return True


if __name__ == '__main__':
    string = [[0,1,0],[1,0,1],[0,1,0]]
    print(removeOnes(string))
