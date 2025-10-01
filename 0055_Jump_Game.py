def canJump(nums):
    last_i = len(nums) - 1

    for i in range(last_i, -1, -1):
        if i + nums[i] >= last_i:
            last_i = i

    return last_i == 0


if __name__ == '__main__':
    inpt = [2,3,1,1,4]
    result = canJump(inpt)
    print(result)



