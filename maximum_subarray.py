i = 0
def maximum_subarray(arr,op):
    sum = temp = 0
    for i in range(len(arr)):
        sum = sum + arr[i]

        if sum > temp:
            temp = sum

        elif sum < 0:
            sum = 0

    print(temp)



if __name__ == '__main__':

    arr = [-2,-3,4,-1,-2,1,5,-3]
    op = []
    maximum_subarray(arr,op)

