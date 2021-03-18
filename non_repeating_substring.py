def non_repeat(inp):
    arr = list(inp)
    end = e = start = s = temp = 0
    op = []
    for i in range(len(arr)):
        if arr[end] not in op:


            op.append(arr[i])
            maxi = max(len(op), temp)
            temp = len(op)
            #start = s
            #e = end
            end = end + 1

        else:
            op=[]
            #s = s + 1
            end = end + 1
            op.append(arr[i])


    print("length is",maxi)
    #print("array",arr[start:end])

if __name__ == '__main__':
    inp = 'pxewwa'
    non_repeat(inp)