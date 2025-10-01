class Solution:
    def exist(self, board, word):
        self.rows = len(board)
        self.cols = len(board[0])
        self.b = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, r, c, suffix):
        if len(suffix) == 0:
            return True

        if r < 0 or r == self.rows or c < 0 or c == self.cols or self.b[r][c] != suffix[0]:
            return False

        ans = False
        self.b[r][c] = "$"

        if self.backtrack(r + 1, c, suffix[1:]) or self.backtrack(r - 1, c, suffix[1:]) or \
                self.backtrack(r, c + 1, suffix[1:]) or self.backtrack(r, c - 1, suffix[1:]):
            return True

        self.b[r][c] = suffix[0]
        return False


if __name__ == '__main__':
    obj = Solution()
    h = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    wrd = "ABCCED"
    result = obj.exist(h, wrd)
    print(result)



