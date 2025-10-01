def fourSumCount(nums1, nums2, nums3, nums4):
    sums = {}
    ans = 0
    for n1 in nums1:
        for n2 in nums2:
            s1 = n1 + n2
            if s1 in sums:
                sums[s1] += 1
            else:
                sums[s1] = 1

    for n3 in nums3:
        for n4 in nums4:
            s2 = n3 + n4
            if -s2 in sums:
                ans += sums[-s2]
    return ans


if __name__ == '__main__':
    ns1 = [1,2]
    ns2 = [-2,-1]
    ns3 = [-1,2]
    ns4 = [0,2]
    result = fourSumCount(ns1, ns2, ns3, ns4)
    print(result)