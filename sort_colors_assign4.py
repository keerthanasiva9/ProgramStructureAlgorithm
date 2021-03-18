#Sort Colors

# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue.

#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]

def sort_colors(arr):

    if len(arr) >1:
        mid = len(arr)//2

        left = arr[:mid]

        right = arr[mid:]

        sort_colors(left)

        sort_colors(right)

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

if __name__ == '__main__':
    arr = [2,0,2,1,1,0]
    print("Unsorted array:",arr)
    sort_colors(arr)
    print("Sorted color:", arr)

