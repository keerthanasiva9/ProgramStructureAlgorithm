class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


def printList(head):
	temp = head
	while temp:
		print(temp.data)
		temp = temp.next

def deleteNodes(head, m, n):

	if head == None or head.next == None:
		return head

	prev_node = None
	current_node = head

	for i in range(1, m + 1):
		prev_node = current_node
		current_node = current_node.next

	for i in range(1, n + 1):
		if current_node:
			next = current_node.next
			current_node = next

	# link remaining nodes with the last node
		prev_node.next = current_node

	# recur for remaining nodes
	deleteNodes(current_node, m, n)

	return prev_node


if __name__ == '__main__':
	head = Node(9)
	head.next = Node(7)
	head.next.next = Node(5)
	head.next.next.next = Node(6)
	head.next.next.next.next = Node(3)
	head.next.next.next.next.next = Node(2)

	head = deleteNodes(head, 1, 1)
	printList(head)
