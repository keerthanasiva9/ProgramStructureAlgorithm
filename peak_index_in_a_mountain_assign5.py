#Peak Index in a Mountain Array

#Let's call an array arr a mountain if the following properties hold:

#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... arr[i-1] < arr[i]
#arr[i] > arr[i+1] > ... > arr[arr.length - 1]

#Input: arr = [0,1,0]
#Output: 1

def peak_index_in_a_mountain_array(arr):
    print("Input array :",arr)
    for i in range(len(arr)):
        if arr[i] > arr[i + 1]:
            print("The peak index in a mountain array is", i)
            pass

if __name__ == '__main__':
    arr = [0,1,0]
    peak_index_in_a_mountain_array(arr)
