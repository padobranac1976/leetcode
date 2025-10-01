import heapq


def findKthLargest(nums, k):
    heap = []
    heapq.heapify(heap)

    for n in nums:
        heapq.heappush(heap, -n)
    return -heapq.nsmallest(k, heap)[-1]


if __name__ == '__main__':
    inpt = [3,2,3,1,2,4,5,5,6]
    result = findKthLargest(inpt, 4)
    print(result)



