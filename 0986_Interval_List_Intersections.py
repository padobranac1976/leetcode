def intervalIntersection(firstList, secondList):
    if len(firstList) == 0 or len(secondList) == 0:
        return []
    start_i, end_i = firstList.pop(0)
    start_j, end_j = secondList.pop(0)
    output = []
    while len(firstList) > 0 or len(secondList) > 0:
        i = max(start_i, start_j)
        j = min(end_i, end_j)
        if i <= j:
            output.append([i, j])
        if end_i > end_j:
            if len(secondList) > 0:
                start_j, end_j = secondList.pop(0)
            else:
                start_i, end_i = firstList.pop(0)
        elif end_i < end_j:
            if len(firstList) > 0:
                start_i, end_i = firstList.pop(0)
            else:
                start_j, end_j = secondList.pop(0)

        else:
            if len(firstList) > 0:
                start_i, end_i = firstList.pop(0)
            if len(secondList) > 0:
                start_j, end_j = secondList.pop(0)

    i = max(start_i, start_j)
    j = min(end_i, end_j)
    if i <= j:
        output.append([i, j])
    return output


if __name__ == '__main__':
    first = [[0,2],[5,10],[13,23],[24,25]]
    second = [[1,5],[8,12],[15,24],[25,26]]
    result = intervalIntersection(first, second)
    print(result)


