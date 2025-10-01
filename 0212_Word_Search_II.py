class Solution:
    def findWords(self, board, words):
        self.whole_word = "$"
        self.trie = {}
        self.board = board
        self.matches = []
        self.rows = len(board)
        self.cols = len(board[0])

        for word in words:
            node = self.trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[self.whole_word] = word

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] in self.trie:
                    self.backtracking(i, j, self.trie)

        return self.matches

    def backtracking(self, r, c, parent):
        if r < 0 or c < 0 or r == self.rows or c == self.cols or self.board[r][c] not in parent:
            return False

        ch = self.board[r][c]
        node = parent[ch]

        match = node.pop(self.whole_word, False)
        if match:
            self.matches.append(match)
        self.board[r][c] = "#"

        self.backtracking(r + 1, c, node)
        self.backtracking(r - 1, c, node)
        self.backtracking(r, c + 1, node)
        self.backtracking(r, c - 1, node)

        self.board[r][c] = ch
        if not node:
            parent.pop(ch)


if __name__ == '__main__':
    obj = Solution()
    h = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    wrd = ["oath","pea","eat","rain"]
    result = obj.findWords(h, wrd)
    print(result)



