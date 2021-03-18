class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insert(self, head, new_node):
        tmp = head
        t_head = head
        prev = head
        while head.data < new_node.data:
            prev = head
            head = head.next
            if head == tmp:
                break
        prev.next = new_node
        new_node.next = head
        while True:
            print(tmp.data)
            tmp = tmp.next
            if tmp == t_head:
                break



l1 = Node(5)
l2 = Node(7)
l3 = Node(8)

l1.next = l2
l2.next = l3
l3.next = l1

l4 = Node(9)

s = Solution()
s.insert(l1, l4)




