class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def removenode(self,rmv_node):
        head_val = self.head

        if head_val is not None:
            if head_val.data == rmv_node:
                print("here")
                self.head = head_val.next
                head_val = None
                return

        while (head_val is not None):
            if head_val.data == rmv_node:
                break

            prev_node = head_val
            head_val = head_val.next

        if (head_val == None):
            return

        #point prev node to the new next node after removing
        prev_node.next = head_val.next
        head_val = None

    def newlistprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next




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

list1.removenode("T")
list1.newlistprint()