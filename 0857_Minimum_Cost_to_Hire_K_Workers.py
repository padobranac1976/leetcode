import heapq


def mincostToHireWorkers(quality, wage, k):
    data = sorted((w/q, q, w) for q, w, in zip(quality, wage))
    ans = float("inf")
    qheap = []
    sumq = 0

    for ratio, q, w in data:
        heapq.heappush(qheap, -q)
        sumq += q

        if len(qheap) > k:
            sumq += heapq.heappop(qheap)

        if len(qheap) == k:
            ans = min(ans, ratio * sumq)

    return ans


if __name__ == '__main__':
    q = [3,1,10,10,1]
    w = [4,8,2,2,7]
    result = mincostToHireWorkers(q, w, 3)
    print(result)



