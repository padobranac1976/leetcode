import random


class Solution:
    def __init__(self, w):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        target = self.total_sum * random.random()

        lo = 0
        hi = len(self.prefix_sum)

        while lo < hi:
            mid = (lo + hi) // 2

            if target > self.prefix_sum[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo


if __name__ == '__main__':
    input1 = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    input2 = [[[1,3]],[],[],[],[],[]]
    output = []
    for i, inpt in enumerate(input1):
        if inpt == "Solution":
            obj = Solution(input2[i][0])
            output.append(None)
        else:
            output.append(obj.pickIndex())

    print(output)


