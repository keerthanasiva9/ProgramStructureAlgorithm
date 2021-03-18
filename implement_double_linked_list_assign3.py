class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkList:
    def add_to_tail(self, head, node):
        tmp = None
        tmp_head = head
        while head is not None:
            tmp = head
            head = head.next
        tmp.next = node
        node.prev = tmp
        return tmp_head

    def add_to_head(self, head, node):
        node.next = head
        head.prev = node
        return node

    def size_of_dll(self, head):
        length = 0
        while head is not None:
            head = head.next
            length = length + 1
        return length

    def print_dll(self, head):
        while head is not None:
            print(head.data)
            head = head.next

if  __name__ == "__main__":

    head = Node(1)
    l1 = Node(2)
    l2 = Node(3)

    head.next = l1
    l1.next = l2
    l1.prev = head
    l2.prev = l1

    d = DoubleLinkList()
    print("print")
    d.print_dll(head)
    print("********")
    print("Add to head")
    h = d.add_to_head(head, Node(0))
    d.print_dll(h)
    print("********")
    print("Add to tail")
    t = d.add_to_tail(h, Node(4))
    d.print_dll(t)

