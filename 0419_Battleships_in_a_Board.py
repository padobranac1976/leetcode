def countBattleships(grid):
    battleships = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                battleships += 1
                is_battleship(i, j, grid)
    return battleships


def is_battleship(i, j, grid):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 'X':
        return
    else:
        grid[i][j] = '.'
        is_battleship(i, j + 1, grid)
        is_battleship(i, j - 1, grid)
        is_battleship(i + 1, j, grid)
        is_battleship(i - 1, j, grid)


if __name__ == '__main__':
    g = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    result = countBattleships(g)
    print(result)


