class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def swapnode(self, l1, res_node):
        res = l1
        d = {}
        length = 1

        while l1 is not None:
            d[length] = l1
            l1 = l1.next
            length = length + 1

        length = length - 1

        x = length - res_node + 1

        d[x].data, d[res_node].data = d[res_node].data, d[x].data

        return d

head = Node(1)
l1 = Node(2)
l2 = Node(3)
l3 = Node(4)
l4 = Node(5)

head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4


k = 2
s = Solution()
result = s.swapnode(head, k)

for key, value in result.items():
    print(value.data)

