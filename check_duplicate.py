def findDuplicates(nums):
    find_dup = []
    arr3 = []

    arr_len = len(nums)

    for num in nums:
        if num not in find_dup:
            find_dup.append(num)
        else:
            arr3.append(num)
    return arr3

if __name__ == "__main__":
    print(findDuplicates([2,3,6,8,4,6,1,4,5,7]))