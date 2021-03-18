def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    arr3 = []
    m = len(nums1)

    n = len(nums2)

    i = j = 0

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            arr3.append(nums1[i])
            print("******")
            i = i + 1
        else:
            arr3.append(nums2[j])
            j = j + 1
    return arr3


if __name__ == "__main__":
    print(merge([2, 3, 6, 8,15], 4, [1, 4, 5, 7,9,13], 4))
