class Solution:
    def numberOfPatterns(self, m, n):
        arr = [['13', 2], ['19', 5], ['17', 4], ['28', 5], ['31', 2], ['37', 5], ['39', 6], ['46', 5], ['79', 8]]
        dct = {}
        for x, y in arr:
            dct[x] = y
            dct[x[::-1]] = y

        self.res = 0

        def helper(arr, prev, seen):
            if m <= len(seen) <= n: self.res += 1
            if len(seen) > n:
                return
            for i, el in enumerate(arr):
                pair = str(prev) + str(el)
                if pair not in dct or (pair in dct and dct[pair] in seen):
                    seen.add(el)
                    helper(arr[:i] + arr[i + 1:], el, seen)
                    seen.remove(el)

        for i in range(1, 10):
            helper([el for el in list(range(1, 10)) if el != i], i, {i})

        return self.res


if __name__ == '__main__':
    obj = Solution()
    result = obj.numberOfPatterns(2,4)
    print(result)



