def searchRange(n, t):
    l = 0
    r = len(n) - 1
    fst_time = True
    found_it = False
    stop_l = False
    stop_r = False

    if len(n) == 1 and n[0] == t:
        return [0, 0]

    while l < r:
        mid = (l + r) // 2
        if n[l] == t or n[r] == t or n[mid] == t:
            found_it = True
            if fst_time:
                fst_time = False
                if n[l] == t and n[r] != t:
                    r = l
                elif n[l] != t and n[r] == t:
                    l = r
                elif n[mid] == t:
                    l = r = mid
            if r + 1 < len(n) and n[r + 1] == t:
                r += 1
            if l - 1 >= 0 and n[l - 1] == t:
                l -= 1
            if r + 1 == len(n) or n[r + 1] != t:
                stop_r = True
            if l - 1 < 0 or n[l - 1] != t:
                stop_l = True
            if stop_l and stop_r:
                break
        elif n[mid] < t:
            l = mid + 1
        elif n[mid] > t:
            r = mid


    if not found_it:
        return [-1, -1]

    return [l, r]


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 6
    result = searchRange(nums, target)
    print(result)


