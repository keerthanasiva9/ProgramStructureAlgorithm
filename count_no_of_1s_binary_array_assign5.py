#Count 1’s in a sorted binary array

#Given a binary array sorted in non-increasing order, count the number of 1’s in it.

#Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
#Output: 2


def no_of_1s(A, left, right):
    if right >= left:

        mid = left + (right - left) // 2

        if ((mid == right or A[mid + 1] == 0) and (A[mid] == 1)):
            return mid + 1

        if A[mid] == 1:
            return no_of_1s(A, (mid + 1), right)

        return no_of_1s(A, left, mid - 1)

    return 0

A = [1, 1, 1, 1, 0, 0, 0]
print("Count of 1's in the array is", no_of_1s(A, 0, len(A) - 1))