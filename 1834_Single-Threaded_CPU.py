import heapq


def getOrder(tasks):
    que = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
    heapq.heapify(que)
    available = []
    current_time = que[0][0]
    processing_order = []

    while que or available:
        while (que and que[0][0] <= current_time) or not available:
            et, pt, i = heapq.heappop(que)
            heapq.heappush(available, [pt, i, et])
        if available:
            pt, i, et = heapq.heappop(available)
            current_time += max(current_time + pt, et + pt)
            processing_order.append(i)
    return processing_order


print(getOrder([[1,2],[2,4],[3,2],[4,1]]))
