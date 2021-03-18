
def main(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        main(left)
        main(right)
        merge(left, right,arr)


def merge(a, b, arr):
    i = j = k = 0
    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            arr[k] = a[i]
            i = i + 1

        else:
            arr[k] = b[j]
            j = j + 1

        k = k + 1


    while i < len(a):
        arr[k] = a[i]
        k = k + 1
        i = i + 1

    while j <len(b):
        arr[k] = b[j]
        j = j + 1
        k = k + 1

    print(arr)

if __name__=='__main__':
    ip1 = [9,1,2,7,4,3,5]

    main(ip1)
