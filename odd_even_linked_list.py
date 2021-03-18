class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def odd_even(self):

        head_val = self.head

        if not head_val:
            return head_val

        odd = head_val
        even = head_val.next
        evenstart = head_val.next

        while odd and even:
            odd.next = even.next

            if not odd.next:
                odd.next = evenstart
                return head_val

            even.next = odd.next.next

            if not even.next:
                odd.next.next = evenstart
                return head_val

            odd, even = odd.next, even.next

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

list1.odd_even()
list1.printList()
