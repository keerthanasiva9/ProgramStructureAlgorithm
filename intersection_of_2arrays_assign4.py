#Intersection Of two arrays

#Given two arrays, write a function to compute their intersection

#Input : nums1 = [4,9,5] , nums2 = [9,4,9,8,4]
#Output : [4,9]

def intersection_of_two_arrays(nums1, nums2):
    print("Array 1 :",nums1)
    print("Array 2:",nums2)
    res = []
    for i in nums1:
        if i in nums2:
            if i not in res:
                res.append(i)
    print("Intersection",res)

if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    intersection_of_two_arrays(nums1,nums2)

