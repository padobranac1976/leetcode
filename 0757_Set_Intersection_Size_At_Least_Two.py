def intersectionSizeTwo(intervals: list[list[int]]) -> int:
    intervals.sort(key = lambda e: (e[1], -e[0]))

    result = [intervals[0][1]-1, intervals[0][1]]

    for a,b in intervals[1:]:

        if result[-2] < a and result[-1] >= a:
            result.append(b)

        elif a > result[-1]:
            result.append(b-1)
            result.append(b)

    return len(result)

if __name__ == '__main__':
    input1 = [[3,13],[2,8],[5,10]]
    input2 = [[],[100],[282],[411],[609],[620],[744],[879],[956],[976],[998],[1055]]
    
    # For function solution
    output = intersectionSizeTwo(input1)
    
    # # For Class solution
    # output = []
    # for i, inpt in enumerate(input1):
    #     if inpt == "HitCounter":
    #         obj = HitCounter()
    #         output.append(None)
    #     elif inpt == "hit":
    #         result = obj.hit(input2[i][0])
    #         output.append(result)
    #     else:
    #         result = obj.getHits(input2[i][0])
    #         output.append(result)

    print(output)



