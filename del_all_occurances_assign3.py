class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def removealloccurance(self,rmv_node):
        head_val = self.head
        prev_node = None

        while head_val is not None and head_val.data == rmv_node:
            self.head = head_val.next
            head_val = self.head


        while (head_val is not None):
            while head_val is not None and head_val.data is not rmv_node:
                prev_node = head_val
                head_val = head_val.next

            if (head_val == None):
                return self.head

             #point prev node to the new next node after removing
            prev_node.next = head_val.next

            head_val = prev_node.next

        return self.head


    def newlistprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next




list1 = LinkedList()
list1.head = Node(6)
l1 = Node(2)
l2 = Node(5)
l3 = Node(4)
l4 = Node(1)
l5 = Node(4)
list1.head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

list1.removealloccurance(4)
list1.newlistprint()