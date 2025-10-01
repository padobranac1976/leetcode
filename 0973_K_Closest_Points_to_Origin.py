import heapq
import math


def kClosest(points, k):
    distance = []
    for i,coord in enumerate(points):
        x, y, = coord
        heapq.heappush(distance, (math.sqrt(x**2+y**2), i))
    output = heapq.nsmallest(k, distance)
    ans = []
    for d, idx in output:
        ans.append(points[idx])
    return ans


def kClosest2(points, k):
    return quick_select(points, k)


def quick_select(points, k):
    l, r = 0, len(points) - 1
    pivot = len(points)
    while pivot != k:
        pivot = partition(points, l, r)
        if pivot < k:
            l = pivot
        else:
            r = pivot
    return points[:k]


def partition(points, left, right):
    pivot = choose_pivot(points, left, right)
    dist = pivot[0]**2 + pivot[1]**2
    while left < right:
        if points[left][0]**2 + points[left][1]**2 >= dist:
            points[left], points[right] = points[right], points[left]
            right -= 1
        else:
            left += 1

    if points[left][0]**2 + points[left][1]**2 < dist:
        left += 1
    return left


def choose_pivot(points, l, r):
    return points[(l+r)//2]


if __name__ == '__main__':
    q = [[1,3],[-2,2]]
    result = kClosest(q, 1)
    print(result)
    result2 = kClosest2(q, 1)
    print(result2)



