# Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    def splitAndPrint(self, h, p):
        c, temp = 0, h

        while temp:
            c, temp = c + 1, temp.next

        div, mod = divmod(c, p)
        i, res = 0, []
        while i < p:
            j, tmp = 0, h
            while j < div - 1:
                if h.next is not None:
                    h = h.next
                j = j + 1
                print(j)

        if div > 0 and mod > 0:
            h, mod = h.next, mod - 1

        if h and (h.next or not h.next):
            newtemp, h.next = h.next, None
            res.append(tmp)
            h = newtemp
        else:
            res.append(None)
        i += 1

        return res

head = Node(9)
head.next = Node(7)
head.next.next = Node(5)
head.next.next.next = Node(6)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(2)

k = 2
s = Solution()
print(s.splitAndPrint(head, k))

