def findMedianSortedArrays(nums1, nums2):
    min_i = 0
    max_i = len(nums1)

    i = (min_i + max_i)//2
    j = (len(nums1) + len(nums2) + 1) // 2 - i
    first_from_A = nums1[:i]
    first_from_B = nums2[:j]
    second_from_A = nums1[i:]
    second_from_B = nums2[j:]

    while first_from_A[-1] > second_from_B[0] or first_from_B[-1] > second_from_A[0]:
        if first_from_A[-1] <= second_from_B[0]:
            min_i = i + 1
        else:
            max_i = i - 1

        i = (min_i + max_i) // 2
        j = (len(nums1) + len(nums2) + 1) // 2 - i
        first_from_A = nums1[:i]
        first_from_B = nums2[:j]
        second_from_A = nums1[i:]
        second_from_B = nums2[j:]

    return max(first_from_A[-1], first_from_B[-1])


if __name__ == '__main__':
    a = [3, 5, 10, 11, 17]
    b = [9, 13, 20, 21, 23, 27]
    output = findMedianSortedArrays(a,b)
    print(output)