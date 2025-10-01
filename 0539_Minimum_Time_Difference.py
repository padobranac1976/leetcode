def findMinDifference(timePoints):
    max_time = float('-infinity')
    sorted_time = [False for i in range(60 * 24)]
    for time in timePoints:
        hr, mins = time.split(":")
        temp = 60 * int(hr) + int(mins)
        if sorted_time[temp] is True:
            return 0
        sorted_time[temp] = True
        max_time = max(temp, max_time)
    last_time = max_time
    curr_diff = float('inf')
    for idx in range(len(sorted_time)):
        if sorted_time[idx] is True:
            curr_diff = min(curr_diff, idx - last_time) % 1440
            last_time = idx
    return curr_diff


print(findMinDifference(["00:00","04:00","22:00"]
))
