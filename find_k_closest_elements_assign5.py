#Find K Closest Elements

'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''

'''
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
'''

import heapq
class Solution:
    def find_close_elements(self,arr, k ,x):
        res = []
        heapq.heapify(res)

        for n in arr:
            difference = abs(x - n)
            heapq.heappush(res, (difference, n))

        return sorted([n[1] for n in heapq.nsmallest(k, res)])

l1 = Solution()

arr = [1,2,3,4,5]
k = 4
x = 3
print(l1.find_close_elements(arr,k,x))





