class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def swap_node(self):

        head_val = self.head

        if not head_val:
            return head_val
        p1 = head_val
        p2 = head_val.next
        while p2:
            p1.data, p2.data = (
                p2.data,
                p1.data
            )
            if not p2.next: break
            p1 = p1.next.next
            p2 = p2.next.next
        return head_val

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

list1 = LinkedList()
list1.head = Node("F")
l1 = Node("I")
l2 = Node("R")
l3 = Node("S")
l4 = Node("T")
list1.head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

print(list1.swap_node())
list1.printList()
