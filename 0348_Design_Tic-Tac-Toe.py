import numpy as np
class TicTacToe:

    def __init__(self, n: int):
        self.grid = np.zeros((n, n)).astype(int)
        self.moves = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.grid[row,col] = player
        self.moves += 1
        return self.determine_winner()

    def determine_winner(self):
        if self.moves < len(self.grid):
            return 0
        
        # check rows and columns
        diagonal_1 = np.zeros(len(self.grid))
        diagonal_2 = np.zeros(len(self.grid))
        for i, r in enumerate(self.grid):
            diagonal_1[i] = r[i]
            diagonal_2[i] = r[-(i+1)]
            if (r == 1).all() or (self.grid[:,i] == 1).all():
                return 1
            if (r == 2).all() or (self.grid[:,i] == 2).all():
                return 2
        
        # diagonals check
        if (diagonal_1 == 1).all() or (diagonal_2 == 1).all():
            return 1
                
        if (diagonal_1 == 2).all() or (diagonal_2 == 2).all():
            return 2
        
        return 0