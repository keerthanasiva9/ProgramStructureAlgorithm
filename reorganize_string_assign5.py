#Reorganize String

#Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.

#Input: S = "aab"
#Output: "aba"

from collections import Counter
import heapq

def reorganize_string(S):
    count = Counter(S)
    heap = [(-value, key) for key, value in count.items()]
    heapq.heapify(heap)
    result = []
    while (len(heap) > 1):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        result.extend([x[1], y[1]])
        if x[0] < -1:
            heapq.heappush(heap, (x[0] + 1, x[1]))
        if y[0] < -1:
            heapq.heappush(heap, (y[0] + 1, y[1]))
    if heap:
        if heap[0][0] < -1:
            print("")
        result.append(heap[0][1])

    str1 = ""

    for i in result:
        str1= str1 + i

    print("The reorganized string is:",str1)


if __name__ == '__main__':
    S = "aab"
    print("Input string is:",S)
    reorganize_string(S)
