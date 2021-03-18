#Given an array and a number k where k is smaller than size of array,
# We need to find the k’th smallest element in the given array.
# It is given that all array elements are distinct

#Input is arr = [11, 9, 17, 2, 34, 8, 56, 85, 12, 10]
# k = 4
#Output = 10

def merge_sort(arr):

    if len(arr) >1:
        mid = len(arr)//2

        left = arr[:mid]

        right = arr[mid:]

        merge_sort(left)

        merge_sort(right)

        i = j = k = 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1

            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1


def nth_smallest(arr,k):
    print("nth smallest element of the array is:",arr[k-1])

if __name__ == '__main__':
    arr = [11,9,17,2,34,8,56,85,12,10]
    print("Unsorted array:",arr)
    k = 4
    merge_sort(arr)

    print("Sorted array:", arr)
    print("The value of n is:", k)
    nth_smallest(arr,k)

