class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def mergeinbetw(self, l1, a, b, l2):
        before_a = l1
        b_next = l1
        list2_tail = l2

        for i in range(b + 1):
            b_next = b_next.next
            if i == a - 2:
                before_a = b_next

        while list2_tail.next:
            list2_tail = list2_tail.next

        before_a.next = l2
        list2_tail.next = b_next

        return l1

    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

head1 = Node(0)
l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)
head1.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

head2 = Node(1000000)
l1 = Node(1000001)
l2 = Node(1000002)
head2.next = l1
l1.next = l2


a = 3
b = 4

LL3 = Solution()
LL3.head = LL3.mergeinbetw(head1, a, b, head2)
LL3.printLL()
