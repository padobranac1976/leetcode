def towSum(nums, target):
    hash_table = {}

    for i, num in enumerate(nums):
        if num in hash_table.keys():
            return [hash_table[num], i]

        hash_table[target-num] = i

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    result = towSum(nums, target)
    print(result)


