def merge(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        merge_sort(left,right,arr)

def merge_sort(left,right,arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
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

    print(arr)



if __name__ == '__main__':
    input_arr=[4,3,5,2,6,1]
    merge(input_arr)