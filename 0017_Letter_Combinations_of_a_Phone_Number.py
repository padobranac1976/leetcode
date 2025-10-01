class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        self.mapping = {"0": " ", "1": "-", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                        "9": "wxyz"}
        self.output = []
        self.backtracking(0, [], digits)
        return self.output

    def backtracking(self, i, build, d):
        if len(build) == len(d):
            self.output.append("".join(build))
            return

        letters = self.mapping[d[i]]
        for l in letters:
            build.append(l)
            self.backtracking(i + 1, build, d)
            build.pop()


if __name__ == '__main__':
    obj = Solution()
    h = "0436010959"
    result = obj.letterCombinations(h)
    print(result)



