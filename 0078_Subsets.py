def subsets(nums):
    sets = [[]]

    for n in nums:
        additional_set = []
        for s in sets:
            new_set = list(s)
            new_set.append(n)
            additional_set.append(new_set)
        sets += additional_set
    return sets


if __name__ == '__main__':
    string = [1,2,3]
    result = subsets(string)
    print(result)