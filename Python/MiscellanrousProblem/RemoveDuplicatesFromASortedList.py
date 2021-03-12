class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def generatePrintableLinkedList(linkedList):
	printableLinkedList = []
	current = linkedList
	while current.next is not None:
		printableLinkedList.append(current.value)
		current = current.next
	return printableLinkedList

def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			nextDistinctNode = nextDistinctNode.next
		
		currentNode.next=nextDistinctNode
		currentNode=nextDistinctNode
		
	return linkedList

# list = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 
list = LinkedList(1)
list.next = LinkedList(1)
list.next.next = LinkedList(3)
list.next.next.next = LinkedList(4)
list.next.next.next.next = LinkedList(4)
list.next.next.next.next.next = LinkedList(4)
list.next.next.next.next.next.next = LinkedList(5)
list.next.next.next.next.next.next.next = LinkedList(6)
list.next.next.next.next.next.next.next.next = LinkedList(6)

print("List Before: ")
print(generatePrintableLinkedList(list))
removeDuplicatesFromLinkedList(list)
print("List After: ")
print(generatePrintableLinkedList(list))