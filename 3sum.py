#Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
#Output: 12, 3, 9
#Explanation: There is a triplet (12, 3 and 9) present
#in the array whose sum is 24.

def threesum(arr,target):
    i = 0
    j = 1
    op=[]
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            x = target - arr[i] - arr[j]
            if x in arr:
                return (arr[i], arr[j], x)
            else:
                continue
    print(op)



if __name__ == "__main__":
    print(threesum([12,3,4,1,6,9],24))

