import heapq

def networkDelayTime(times, n, k):
    adj_list = {}

    for x, y, w in times:
        if x in adj_list:
            adj_list[x].append((w, y))
        else:
            adj_list[x] = [(w, y)]

    visited = set()
    heap = [(0, k)]
    while heap:
        travel_time, node = heapq.heappop(heap)
        visited.add(node)

        if len(visited) == n:
            return travel_time

        if node not in adj_list:
            continue
        for time, adjacent_node in adj_list[node]:
            if adjacent_node not in visited:
                heapq.heappush(heap, (travel_time + time, adjacent_node))

    return -1


if __name__ == '__main__':
    input1 = [[2,1,1],[2,3,1],[3,4,1]]
    print(networkDelayTime(input1, 4, 2))