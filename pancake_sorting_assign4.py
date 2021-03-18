#Pancake Sorting

#Given an array of integers arr, sort the array by performing a series of pancake flips.

#Input: nums = [3,2,4,1]
#Output: [3,4,2,3,1,2]

def pancake_sorting(arr):
    result = []
    end = len(arr)
    while end > 0:
        maximum = max(arr[:end])
        max_index = arr[:end].index(maximum)
        if max_index + 1 == end:
            end = end - 1
        else:
            result.append(max_index + 1)
            arr[:max_index + 1] = arr[:max_index + 1][::-1]
            result.append(end)
            arr[:end] = arr[:end][::-1]
            end = end - 1
    print("Sorted array after pancake flips:",result)

if __name__ == '__main__':
    arr = [3,2,4,1]
    print("Unsorted array:",arr)
    pancake_sorting(arr)

