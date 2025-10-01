def solve(board):
    if not board or not board[0]:
        return

    ROWS = len(board)
    COLS = len(board[0])

    for i in range(ROWS):
        for j in range(COLS):
            if i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1:
                DFS(board, i, j)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O':
                board[r][c] = "X"
            elif board[r][c] == "E":
                board[r][c] = "O"
    return board

def DFS(board, i, j):
    if board[i][j] != "O":
        return
    board[i][j] = "E"
    if i > 0:
        DFS(board, i - 1, j)
    if i < len(board) - 1:
        DFS(board, i + 1, j)
    if j > 0:
        DFS(board, i, j - 1)
    if j < len(board[0]) - 1:
        DFS(board, i, j + 1)


if __name__ == '__main__':
    g = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    result = solve(g)
    print(result)


