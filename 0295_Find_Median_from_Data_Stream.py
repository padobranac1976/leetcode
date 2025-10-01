import heapq as hq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        hq.heapify(self.minHeap)
        self.maxHeap = []
        hq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        hq.heappush(self.maxHeap, -num)
        hq.heappush(self.minHeap, -hq.heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            hq.heappush(self.maxHeap, -hq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) * .5
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    input1 = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    input2 = [[], [1], [2], [], [3], []]
    output = []

    for i, command in enumerate(input1):
        if command == "MedianFinder":
            obj = MedianFinder()
            output.append(None)
        elif command == "addNum":
            output.append(obj.addNum(input2[i][0]))
        elif command == "findMedian":
            output.append(obj.findMedian())
    print(output)