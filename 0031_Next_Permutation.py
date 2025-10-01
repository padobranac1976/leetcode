def nextPermutation(nums):
    if len(nums) < 2:
        pass
    elif len(nums) < 3:
        nums = nums[::-1]
    else:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        if i == 0 and nums[0] > nums[i+1]:
            nums.sort()

        else:
            curr_val = nums[i]
            min_diff = float("inf")
            target = i + 1
            for j in range(target, len(nums)):
                if 0 < nums[j] - curr_val <= min_diff:
                    target = j
                    min_diff = nums[j] - curr_val
            nums[i] = nums[target]
            nums[target] = curr_val
            nums[i+1:] = nums[i+1:][::-1]
    return nums

if __name__ == '__main__':
    n = [2,3,1,3,3]
    result = nextPermutation(n)
    print(result)


