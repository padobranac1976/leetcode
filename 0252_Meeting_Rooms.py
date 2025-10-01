def canAttendMeetings(intervals):
    intervals.sort()

    for i in range(len(intervals) - 1):
        s1, e1 = intervals[i]
        s2, e2 = intervals[i + 1]
        if e1 > s2:
            return False
    return True


if __name__ == '__main__':
    inpt = [[7,10],[2,4]]
    result = canAttendMeetings(inpt)
    print(result)



