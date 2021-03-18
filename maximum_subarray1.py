i = k = 0

def maximum_subarray(arr, op):
    start = end = s = 0
    sum = temp = 0
    for i in range(len(arr)):
        sum = sum + arr[i]

        if sum > temp:
            temp = sum
            start = s
            end = i


        elif sum < 0:
            sum = 0
            s = s + 1

        maxi = max(sum,temp)


        for k in range(start,end):
           op.append(arr[k])
            
    print(arr[start:end+1])
    print("maximum sum",maxi)
    print("starting index",start)
    print('ending index',end)


if __name__ == '__main__':
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    op = []
    maximum_subarray(arr, op)

