from sortedcontainers import SortedList


def minMeetingRooms(intervals):
    end = SortedList()
    start = SortedList()
    for s, e in intervals:
        end.add(e)
        start.add(s)

    i = j = 0
    used = 0
    while i < len(start):
        if start[i] >= end[j]:
            used -= 1
            j += 1
        used += 1
        i += 1
    return used


if __name__ == '__main__':
    inpt = [[7,10],[2,4]]
    result = minMeetingRooms(inpt)
    print(result)



