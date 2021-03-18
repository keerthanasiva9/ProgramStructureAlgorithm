#Given a sorted array of integers containing duplicates, write a program which returns the last index of an element.

#Example:
#Input:
#array = {0, 1, 2, 2, 4, 5, 5, 5, 8};
#num = 5;
#Output:
#Element 5 found at index 7

def index_element(arr,num):
    ind = 0
    for i in range(len(arr)):
        if arr[i] == num:
            ind = i

    return ind


if __name__ == "__main__":
    print(index_element([0,1,2,2,4,5,5,5,8],5))